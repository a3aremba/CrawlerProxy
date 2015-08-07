# -*- coding: utf-8 -*-
from core.consts.session_params import SESSION_PHONE
from core.extras.otp.Otp import COtp
from core.logic.response import ApiInternalServerErrorResponse
from core.lib.kibanaLog import CKibanaLog


class AuthorizationClient(object):
    def __init__(self, request, sessionInfo, merchant_id, operation=None, merchant_params=None):
        self.reqtype = request.POST.get('reqtype')
        self.sessionInfo = sessionInfo
        self.merchant_id = merchant_id
        self.merchant_params = merchant_params
        self.isSuccess = False
        self.response = None
        self.operation = operation
        self.request_POST = request.POST

    def callAuth(self):
        self.isSuccess, self.response = self.authOtp()
        return self.isSuccess, self.response

    def authOtp(self):
        if self.reqtype == 'phone':
            otp = COtp(sessionInfo=self.sessionInfo, merchant_id=self.merchant_id, merchant_params=self.merchant_params,
                       phone=self.sessionInfo.getParam(SESSION_PHONE), operation=self.operation)
            self.isSuccess, self.response = otp.setOtpPhone()
            self.isSuccess = False
            return self.isSuccess, self.response
        if self.reqtype == 'otpcode':
            otp = COtp(sessionInfo=self.sessionInfo, merchant_id=self.merchant_id)
            self.isSuccess, self.sessionInfo, self.response = otp.setOtpCode()
            return self.isSuccess, self.response
        CKibanaLog({'fileError': 'AuthorizationClient',
                    'reqtype': self.reqtype,
                    'request_POST': dict(self.request_POST),
                    'merchant_id': self.merchant_id,
                    'operation': self.operation,
        })
        api_response = ApiInternalServerErrorResponse(u'Ошибка авторизации')
        return False, api_response.response