from pyscript import document, display


def orderaccept(e):
    ish = document.getElementById("amer")
    hea = document.getElementById("spain")
    sin = document.getElementById("cold")
    don = document.getElementById("cappu")
    meu = document.getElementById("caramel")

    subtotal = (
    (float(ish.value) if ish.checked else 0.0)
    +(float(hea.value) if hea.checked else 0.0)
    +(float(sin.value) if sin.checked else 0.0)
    +(float(don.value) if don.checked else 0.0)
    +(float(meu.value) if meu.checked else 0.0)
    
    )

    #Checks each box if it was clicked on then adds the value to the receipt, if not, then the value added remains 0.

    vat = subtotal * 0.12

    #Adds the tax to the total.

    output = f""" 
    ====Receipt====<br> 
    Subtotal: ₱{subtotal}<br>
    VAT: ₱{vat}<br>
    Total: ₱{subtotal + vat}<br>
    """
    #Creates the receipt for the receipt generator.

    document.getElementById("textoutput").innerHTML = output

def makeSKU(e):
    document.getElementById('SKUGEN').innerHTML = ""
    cavar = document.getElementById('category').value
    navar = document.getElementById('name').value.strip()
    quvar = document.getElementById('quantity').value.strip()
    SKUname = prodCategory.upper() + "-" + prodName.upper + "-" + prodQty

    #Gets the variable and it's value and uses it for the generator's receipt

    display("SKU: ", SKUname, target='SKUGEN')

    #Displays the SKU generator receipts.
