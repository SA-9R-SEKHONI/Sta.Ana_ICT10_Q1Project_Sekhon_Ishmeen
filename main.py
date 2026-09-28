from pyscript import document


def SKU_generator(event):
    """
    Builds a unique SKU (max 8 alphanumeric characters) out of:
    - first 3 letters of the Category
    - first 3 letters of the Product Name
    - a 2-digit code derived from the Stock Quantity

    Example: Category "Earrings", Product "Stud earrings", Qty 50 -> "EARSTU50"
    """
    category_el = document.getElementById("category")
    product_el = document.getElementById("product_name")
    quantity_el = document.getElementById("quantity")
    output = document.getElementById("sku_output")

    category = category_el.value
    product_name = product_el.value.strip()
    quantity_raw = quantity_el.value.strip()

    if not product_name or not quantity_raw:
        output.innerHTML = (
            '<p class="text-danger text-center mb-0">'
            'Please fill in the product name and stock quantity.</p>'
        )
        return

    try:
        quantity = int(quantity_raw)
        if quantity < 0:
            raise ValueError
    except ValueError:
        output.innerHTML = (
            '<p class="text-danger text-center mb-0">'
            'Stock quantity must be a whole number of 0 or more.</p>'
        )
        return
    
    cat_letters = "".join(ch for ch in category.upper() if ch.isalpha())
    cat_code = (cat_letters + "XXX")[:3]


    prod_letters = "".join(ch for ch in product_name.upper() if ch.isalpha())
    prod_code = (prod_letters + "XXX")[:3]


    qty_code = str(quantity).zfill(2)[-2:]

    sku = f"{cat_code}{prod_code}{qty_code}"

    output.innerHTML = f'''
    <div class="result-box">
        <p class="mb-1 text-muted">Generated SKU for <strong>{product_name}</strong>:</p>
        <div class="sku-code">{sku}</div>
        <small class="text-muted">
            Category: {category} &bull; Stock: {quantity} unit(s)
        </small>
    </div>
    '''


def create_order(event):
    """
    Reads the checked items on the Ives accessories menu, adds up their
    prices, and prints an itemized receipt with a grand total.
    """
    items = [
        ("item1", "Bahubali Earrings"),
        ("item2", "Stud Earrings"),
        ("item3", "Kashmiri Bangles Set"),
        ("item4", "Layered Necklace"),
        ("item5", "Rani Haar"),
        ("item6", "Payal / Jhanjar"),
        ("item7", "Bichiya Rings"),
        ("item8", "Finger Rings"),
        ("item9", "Sampaguita Hair Comb"),
        ("item10", "Gajra"),
        ("item11", "Potli Bag"),
        ("item12", "Banig Bag"),
    ]

    show = document.getElementById("show")

    selected = []
    total = 0

    for item_id, name in items:
        checkbox = document.getElementById(item_id)
        if checkbox.checked:
            price = int(checkbox.value)
            selected.append((name, price))
            total += price

    if not selected:
        show.innerHTML = (
            '<p class="text-danger text-center mb-0">'
            'Please select at least one item.</p>'
        )
        return

    rows = "".join(
        f'<div class="d-flex justify-content-between">'
        f'<span>{name}</span><span>&#8369;{price}</span></div>'
        for name, price in selected
    )

    show.innerHTML = f'''
    <div class="result-box">
        <p class="mb-2 fw-bold">Order Receipt</p>
        {rows}
        <hr>
        <div class="d-flex justify-content-between receipt-total">
            <span>Total</span><span>&#8369;{total}</span>
        </div>
    </div>
    '''