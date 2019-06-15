function getCookie(c_name){
    if (document.cookie.length > 0){
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1){
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
}


function add_button(elem, direction, id, status){
    var button = document.createElement("button");
    button.id = "button_"+ direction + "_" + id;
    if (direction === 'left'){
        button.setAttribute('onclick', "change_status(" + id + ", '" + status + "')");
        button.innerHTML = '<<<';
        elem[0].firstElementChild.parentNode.insertBefore(button, elem[0].firstElementChild)

    } else if (direction === 'right'){
        button.setAttribute('onclick', "change_status(" + id + ", '" + status + "')");
        button.innerHTML = '>>>';
        elem[0].lastElementChild.parentNode.insertBefore(button, elem[0].lastElementChild)
      }
    return button
}

function change_status(id, status) {
        $.ajaxSetup({
            headers: { "X-CSRFToken": getCookie("csrftoken") }
        });
        $.ajax({
            type: 'POST',
            url: '/card/status/',
            data: {'id': id, 'status': status},
            dataType: "json",
            success: function (data) {
                if (data.success === '1') {
                    var elem = $('#' + 'card_' + id);
                    $('button[id=button_left_' + id + ']').remove();
                    $('button[id=button_right_' + id + ']').remove();
                    switch (status) {
                        case '0':
                            add_button(elem, 'right', id, 1);
                            break;
                        case '1':
                            add_button(elem, 'left', id, 0);
                            add_button(elem, 'right', id, 2);
                            break;
                        case '2':
                            add_button(elem, 'left', id, 1);
                    }

                    elem.detach().appendTo("#" + "column_" + status);
                }
            }
        });
}


$(document).ready(function () {
    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });
    $(document).on('click','button.delete-card', {}, function(e){
        e.defaultPrevented = true;
        var elem = $(this);
        var card_id = $(this).attr('value');
        console.log(card_id);
        console.log(elem);

        $.ajax({
                type: 'POST',
                url: '/card/delete/',
                data: {'id': card_id},
                dataType: 'json',
                success: function (data) {
                        if (data.success === '1'){
                            elem.prev().prev().prev().remove();
                            elem.prev().prev().remove();
                            elem.prev().remove();
                            elem.remove();
                        }
                }
            });
    })
});