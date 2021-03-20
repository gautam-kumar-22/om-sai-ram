"""Extra functionality."""
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

def send_email_to_admin(ctx):
	"""Send email."""
	subject = 'New Enquiry'
	name = ctx.get('name')
	to_email = settings.EMAIL_HOST_USER
	from_email = ctx.get('email')
	context = {
		'name': ctx.get('name'),
		'phone_number': ctx.get('phone_number'),
		'email': ctx.get('email'),
		'address': ctx.get('address'),
		'product': ctx.get('product'),
		'brand': ctx.get('brand'),
		'service': ctx.get('service'),
		'message': ctx.get('message'),
	}
	try:
		message = render_to_string('email.html', context)
		msg = EmailMultiAlternatives(subject, message, from_email, [to_email])
		msg.attach_alternative(message, "text/html")
		msg.content_sub_type = 'html'
		msg.send()
	except:
		pass
