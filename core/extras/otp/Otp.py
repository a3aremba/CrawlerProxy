# -*- coding: utf-8 -*-
from core.utils import isGet
from core.consts.session_params import SESSION_PHONE
from OtpPhone import COtpPhone
from core.logic.response import ApiInternalServerErrorResponse, ApiSuccessResponse


class COtp(object):
    def __init__(self, sessionInfo, merchant_id=None, merchant_params=None, phone=None, request=None, operation=None):
        self.sessionInfo = sessionInfo
        self.merchant_id = merchant_id
        self.merchant_params = merchant_params
        self.phone = phone
        self.request = request
        self.operation = operation
        self._errorTitle = ''
        self._errorText = ''

    def setOtpPhone(self, merchant_id=None):
        if merchant_id is None:
            merchant_id = self.merchant_id

        phoneNumber = self.getPhone()
        otp_phone = COtpPhone(phoneNumber=phoneNumber, merchant_id=merchant_id, merchant_params=self.merchant_params,
                              request=self.request, sessionInfo=self.sessionInfo, operation=self.operation)

        isSuccess = otp_phone.sendPhone()
        #isSuccess = True

        if isSuccess:
            request_params = dict(self.sessionInfo.request.REQUEST)
            response = ApiSuccessResponse(request_params).response
        else:
            api_response = ApiInternalServerErrorResponse(otp_phone.errorText)
            api_response.user_title = otp_phone.errorTitle
            api_response.developer_code = 'phone'
            response = api_response.response
        return isSuccess, response

    def setOtpCode(self, merchant_id=None):
        if merchant_id is None:
            merchant_id = self.merchant_id

        userOtpPas = isGet(self.sessionInfo.request.POST.getlist('otpcode'))

        phoneNumber = self.getPhone()

        otp_phone = COtpPhone(phoneNumber=phoneNumber, merchant_id=merchant_id, sessionInfo=self.sessionInfo)
        isSuccess = otp_phone.verifyPassword(userOtpPas)
        #isSuccess = True

        if isSuccess:
            response = None
        else:
            self._errorTitle = otp_phone.errorTitle
            self._errorText = otp_phone.errorText
            api_response = ApiInternalServerErrorResponse(otp_phone.errorText)
            api_response.user_title = otp_phone.errorTitle
            api_response.developer_code = 'otpcode'
            response = api_response.response
        return isSuccess, self.sessionInfo, response

    def getPhone(self):
        phoneNumber = self.sessionInfo.getParam(SESSION_PHONE)
        return self.__getClearPhoneNumber(phoneNumber=phoneNumber)

    def __getClearPhoneNumber(self, phoneNumber=None):
        if phoneNumber is None:
            phoneNumber = self.phone

        clearPhoneNumber = phoneNumber
        for elem in ['(', ')', ' ', '-']:
            clearPhoneNumber = clearPhoneNumber.replace(elem, '')
        return clearPhoneNumber