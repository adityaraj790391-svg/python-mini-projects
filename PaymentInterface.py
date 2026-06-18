import qrcode

# Taking UPI ID as input from the user

upi_id = input("Enter your UPI ID: ")

# upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

# Defning the payment URL based on the UPI ID and the payment app
# Ypu can modify these URLs based on the payment apps you want to support

phonepe_url = f"upi://pay?pa={upi_id}&pn=YourName&am=10&cu=INR&tn=Payment for services"
gpay_url = f"upi://pay?pa={upi_id}&pn=YourName&am=10&cu=INR&tn=Payment for services"
paytm_url = f"upi://pay?pa={upi_id}&pn=YourName&am=10&cu=INR&tn=Payment for services"

# Generating QR codes for each payment app

phonepe_qr = qrcode.make(phonepe_url)
gpay_qr = qrcode.make(gpay_url)
paytm_qr = qrcode.make(paytm_url)

# Saving the QR codes as images

phonepe_qr.save("phonepe_qr.png")
gpay_qr.save("gpay_qr.png")
paytm_qr.save("paytm_qr.png")

# Displaying the QR codes using pillow library

phonepe_qr.show()

