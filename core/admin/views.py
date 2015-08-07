# -*- coding: utf-8 -*-
__author__ = 'alexz'

import json
from django.http import HttpResponse
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from core.service.UrlTracker.TrackerManagerService.TrackerManager import CTrackerManagerService
from core.model_managers.GroupRuleManager import CGroupRuleManager

def track_and_save_rule(request, product_id):
    params = {'title': 'Track and Save',
              'product_id': product_id}
    response = render_to_response('admin/admin_track_rule_template.html', params,
                                  RequestContext(request))
    return response

def collector_start(request, product_id):
    tracker_manger = CTrackerManagerService(product_id)
    return HttpResponse(json.dumps(tracker_manger.start_tracker()),
                        content_type="application/json")

def collector_stop(request, product_id):
    tracker_manger = CTrackerManagerService(product_id)
    return HttpResponse(json.dumps(tracker_manger.stop_tracker()),
                        content_type="application/json")

def collector_collect(request, product_id):
    tracker_manger = CTrackerManagerService(product_id)
    return HttpResponse(json.dumps(tracker_manger.get_collect()),
                        content_type="application/json")

def collector_clear(request, product_id):
    tracker_manger = CTrackerManagerService(product_id)
    tracker_manger.clear_buffer()
    return HttpResponse(json.dumps(tracker_manger.get_message()),
                        content_type="application/json")

def collector_make_rules(request, product_id):
    tracker_manger = CTrackerManagerService(product_id)
    new_rules = tracker_manger.make_rule()
    tracker_manger.stop_tracker()
    tracker_manger.clear_buffer()
    params = {'created_rules': [],
              'product_id': product_id}
    if new_rules.get('status'):
        params['created_rules'] = new_rules.get('created_rules')
    else:
        params['error'] = new_rules.get('message')

    return render_to_response('admin/create_new_rules.html', params,
                                  RequestContext(request))

def return_from_collect(request, product_id):
    tracker_manger = CTrackerManagerService(product_id)
    tracker_manger.stop_tracker()
    tracker_manger.clear_buffer()
    return redirect('admin:core_product_change', product_id)

# for saving activate grouping
def activate_and_save(request):
    id = request.GET.dict().get('id')
    type = request.GET.dict().get('type')
    try:
        toogle = not bool(int(request.GET.dict().get('toggle')))  # Revert value for changing the value in db
    except Exception, e:
        toogle = False

    group_rule_manager = CGroupRuleManager()
    if type == 'group':
        answer_response = group_rule_manager.toggle_group(id, toogle)
    elif type == 'rule':
        answer_response = group_rule_manager.toggle_rule_by_id(id, toogle)
    else:
        answer_response = {'status': False,
                           'message': "type is incorrect",
                           'values': []}

    return HttpResponse(json.dumps(answer_response),
                        content_type="application/json")