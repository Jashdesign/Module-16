from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from .checksum import generate_checksum, verify_checksum

def initiate_payment(request):
    order_id = "ORDER123"
    amount = "100.00"

    paytm_params = {
        "MID": settings.PAYTM_MERCHANT_ID,
        "ORDER_ID": order_id,
        "CUST_ID": "CUST001",
        "TXN_AMOUNT": amount,
        "CHANNEL_ID": settings.PAYTM_CHANNEL_ID,
        "WEBSITE": settings.PAYTM_WEBSITE,
        "INDUSTRY_TYPE_ID": settings.PAYTM_INDUSTRY_TYPE_ID,
        "CALLBACK_URL": settings.PAYTM_CALLBACK_URL,
    }

    checksum = generate_checksum(paytm_params, settings.PAYTM_MERCHANT_KEY)
    paytm_params["CHECKSUMHASH"] = checksum

    return render(request, "pay.html", {"paytm_params": paytm_params})

def callback(request):
    received_data = request.POST.dict()
    checksum = received_data.pop("CHECKSUMHASH", "")

    is_valid = verify_checksum(
        received_data,
        settings.PAYTM_MERCHANT_KEY,
        checksum
    )

    if is_valid and received_data.get("RESPCODE") == "01":
        return HttpResponse("Payment Successful")
    else:
        return HttpResponse("Payment Failed")