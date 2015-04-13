jQuery(document).ready(function($) {
	$('#ajaxButton').click(function(event) {
		$.ajax({
				url: 'http://localhost:9999/getChart/',
				type: 'GET',
				dataType: 'json',
				data: {param1: 'value1'},
			})
			.done(function() {
				console.log("success");
			})
			.fail(function() {
				console.log("error");
			})
			.always(function() {
				console.log("complete");
			});
				
	});
});