function Register(event){
	event.preventDefault();


	$.ajax({
		url: '/announce/',
		type: 'POST',
		data: { msgbox: $('#newd').val() },

		success: function(json){
			$('#newd').val('');
			$('#test').append('<li class="list-group-item">'+json.msg+'</li>');

		}
	});
}


// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});



// function getMessages(){
// 	$.get('/announcementss/',function(messages){
// 		$('#test').html(messages);
// 	});
// }
// $(function(){
// 	$('#rpa').on('hover',function(){
// 		refreshTimer = setInterval(getMessages,500);
// 	});
// });