# -*- coding: utf-8 -*-
import string
from core.consts.session_params import SESSION_BANK
from core.webservices.OTPServices.otp import OTPInterface
from core.models import OtpMerchant

reqTypeId = 'type_id'
reqDepSum = 'dep_sum'


class COtpPhone(object):
    def __init__(self, phoneNumber, merchant_id, merchant_params=None, request=None, sessionInfo=None, operation=None):
        self.__phoneNumber = phoneNumber
        self.__setClearPhoneNumber()
        self.errorTitle = ''
        self.errorText = ''
        self.__merchant_id = merchant_id
        self.__merchant_params = merchant_params
        self.__request = request
        self.sessionInfo = sessionInfo
        self.operation = operation


    def __setClearPhoneNumber(self, phoneNumber=None):
        if phoneNumber is None:
            phoneNumber = self.__phoneNumber

        clearPhoneNumber = phoneNumber
        for elem in ['(', ')', ' ', '-']:
            clearPhoneNumber = clearPhoneNumber.replace(elem, '')

        self.__clearPhoneNumber = clearPhoneNumber

    def getClearPhone(self):
        return self.__clearPhoneNumber

    # подставка в смс параметров
    def __inserts_params_to_sms_text_start(self):
        if not self.__merchant_params or not self.__smsTextStart:
            return
        if string.count(self.__smsTextStart, '%s') == len(self.__merchant_params):
            self.__smsTextStart = self.__merchant.sms_text_start % self.__merchant_params
        return

    def sendPhone(self):
        self.__merchant = self.__selectMerchant()
        self.__merchant_password = self.__merchant.merchant_password
        self.__smsTextStart = self.__merchant.sms_text_start
        self.__inserts_params_to_sms_text_start()
        self.__smsTextEnd = self.__merchant.sms_text_end

        otpInterface = OTPInterface(phone=self.__clearPhoneNumber, merchant_id=self.__merchant_id,
                                    merchant_password=self.__merchant_password, smsTextStart=self.__smsTextStart,
                                    smsTextEnd=self.__smsTextEnd, sesssionInfo=self.sessionInfo)
        isSuccess = otpInterface.sendPassword()
        self.errorTitle = otpInterface.getErrorTitle()
        self.errorText = otpInterface.getErrorText()

        return isSuccess


    def verifyPassword(self, userOtpPassword):
        self.__merchant = self.__selectMerchant()
        self.__merchant_password = self.__merchant.merchant_password

        otpInterface = OTPInterface(phone=self.__clearPhoneNumber, merchant_id=self.__merchant_id,
                                    merchant_password=self.__merchant_password, sesssionInfo=self.sessionInfo)
        isSuccess = otpInterface.verifyPassword(userOtpPassword)
        self.errorTitle = otpInterface.getErrorTitle()
        self.errorText = otpInterface.getErrorText()

        return isSuccess


    def __selectMerchant(self, merchant_id=None):
        if merchant_id is None:
            merchant_id = self.__merchant_id
        bank = self.sessionInfo.getParam(SESSION_BANK)
        merchant = OtpMerchant.objects.get(merchant_id=merchant_id, merchant_bank=bank)
        return merchant