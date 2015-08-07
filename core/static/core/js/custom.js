/**
 * Created by alexz on 09.12.14.
 */
$(on_change_fix);

function on_change_fix() {

    $('.request-data').change(checked_and_send_method);
    $('.toggle_activate').click(toggle_activate_group);
    $('#id_request_ANY').click(function () {
        set_ALL(false);
    });

};

function checked_and_send_method() {
    if (check_is_one_more_checked()) {
        set_ANY(false);
    } else {
        set_ANY(true);
    }
}

function set_ANY(status) {
    $('#id_request_ANY').prop('checked', status)
};

function check_is_one_more_checked() {
     return ($('#id_request_GET').prop('checked') || $('#id_request_POST').prop('checked') ||
            $('#id_request_PUT').prop('checked') || $('#id_request_DELETE').prop('checked') ||
            $('#id_request_HEAD').prop('checked') || $('#id_request_PATCH').prop('checked') ||
            $('#id_request_TRACE').prop('checked') || $('#id_request_CONNECT').prop('checked') ||
            $('#id_request_OPTIONS').prop('checked') )
}

function set_ALL(status) {
    $('#id_request_GET, #id_request_POST, #id_request_PUT, #id_request_DELETE, #id_request_HEAD, #id_request_PATCH, #id_request_TRACE, #id_request_CONNECT, #id_request_OPTIONS').prop('checked', status);
}

function toggle_activate_group() {
    var group_id = $(this).attr('data-id');
    var toggle = $(this).attr('alt') == 'True' ? 1 : 0;
    var type =  $(this).attr('data-type');

    var request = $.ajax({
      url: "activate-save-group/",
      type: "GET",
      data: {'id': group_id,
             'type': type,
             'toggle':toggle },
      dataType: "json"
    });

    request.done(function( response ) {
        if (!response.status) {
            alert("we have data error: " + response.message)
            return false
        }
        $.each(response.values, function(i, item) {
            toggle_object(item.type, item.id, item.value)
        })
    });

    request.fail(function( jqXHR, textStatus ) {
      alert( "Request failed: " + textStatus );
    });
}

function toggle_object(type, id, value) {
    need_element = '#'+type+'_'+id;
    if (value) {
        $(need_element).attr("src","/static/admin/img/icon-yes.gif");
        $(need_element).attr("alt", "True")
    } else {
        $(need_element).attr("src","/static/admin/img/icon-no.gif");
        $(need_element).attr("alt", "False")
    }
}

