#!/root/Python-3.5.2/python 
# Author: Miroslav Houdek miroslav.houdek at gmail dot com
# License is, do whatever you wanna do with it (at least I think that that is what LGPL v3 says)
#
from ipvalidator import *
from rblquery import *
import sys
sys.path.append('/tmp/postfixmitler/')
import asyncore
import asynchat
from new_smtplib import *
import traceback

class CustomSMTPServer(new_SMTPServer):

	def process_message(self, peer, mailfrom, rcpttos, data, x_forward, **kwargs):
		print('Starting')
		mailfrom.replace('\'', '')
		mailfrom.replace('\"', '')
		ip='2.2.2.2'
		print(IPValidator().validate_ip(ip))
		print('1 done')
		print(IPValidator().reverse_ip('4.3.2.1'))
		print('2 done')
		print(Query().rbl_lookup(ip))
		print('3 done')
		ip='4.4.4.4'
		print(Query().rbl_lookup(ip))
		print('4 done')
		ip='5.5.5.5'
		print(Query().rbl_lookup(ip))
		print('5 done')

		for recipient in rcpttos:
			recipient.replace('\'', '')
			recipient.replace('\"', '')
		print ('Receiving message from:', peer)
		print ('Message addressed from:', mailfrom)
		print ('Message addressed to  :', rcpttos)
		print ('MSG >>')
		print (data)
		if ("PROTO" in data):
			print('BOOM HERE COMES THE BOOM')
		print ('>> EOT')
		print('Xforward Headers: ' + x_forward)

		try:
			# DO WHAT YOU WANNA DO WITH THE EMAIL HERE
			# In future I'd like to include some more functions for users convenience, 
			# such as functions to change fields within the body (From, Reply-to etc), 
			# and/or to send error codes/mails back to Postfix.
			# Error handling is not really fantastic either.
                        print ('Boom')
                        pass
		except:
			pass
			print ('Something went south')
			print (traceback.format_exc())

		try:
                        server = smtplib.SMTP('localhost', 10026)
                        print(rcpttos)
                        server.sendmail(mailfrom, rcpttos, data)
                        server.quit()
                        print ('send successful')
		except smtplib.SMTPException:
			print ('Exception SMTPException')
			pass
		except smtplib.SMTPServerDisconnected:
			print ('Exception SMTPServerDisconnected')
			pass
		except smtplib.SMTPResponseException:
			print ('Exception SMTPResponseException')
			pass		
		except smtplib.SMTPSenderRefused:
			print ('Exception SMTPSenderRefused')
			pass		
		except smtplib.SMTPRecipientsRefused:
			print ('Exception SMTPRecipientsRefused')
			pass		
		except smtplib.SMTPDataError:
			print ('Exception SMTPDataError')
			pass		
		except smtplib.SMTPConnectError:
			print ('Exception SMTPConnectError')
			pass		
		except smtplib.SMTPHeloError:
			print ('Exception SMTPHeloError')
			pass		
		except smtplib.SMTPAuthenticationError:
			print ('Exception SMTPAuthenticationError')
			pass
		except:
			print ('Undefined exception')
			print (traceback.format_exc())

		return
		
server = CustomSMTPServer(('127.0.0.1', 10025), None)
print('test')
asyncore.loop()
