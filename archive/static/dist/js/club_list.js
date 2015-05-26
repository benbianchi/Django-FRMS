$(function() {
	
	$('#searchFilter').keyup(function(event) {
		var list = $('.data')
		$.each(list,function(index, item){
			if ((item.innerHTML.indexOf(	$('#searchFilter').val()	)) > -1)
				item.className = "data animated slideInLeft"
			else
				item.className = "hidden data animated slideInLeft"
		});
	});

	// $("#SortNameGlyph").click(function(event) {
		
	// 	if ($(this).attr('class') == "glyphicon glyphicon-circle-arrow-down")
			
	// 		$(this).attr('class',"glyphicon glyphicon-circle-arrow-up")
	// 	else
	// 		$(this).attr('class',"glyphicon glyphicon-circle-arrow-down")

	// });

	// $("#SortPurposeGlyph").click(function(event) {
	// 	if ($(this).attr('class') == "glyphicon glyphicon-circle-arrow-down")
			
	// 		$(this).attr('class',"glyphicon glyphicon-circle-arrow-up")
	// 	else
	// 		$(this).attr('class',"glyphicon glyphicon-circle-arrow-down")

	// });

	// $("#SortClassGlyph").click(function(event) {
	// 	if ($(this).attr('class') == "glyphicon glyphicon-circle-arrow-down")
			
	// 		$(this).attr('class',"glyphicon glyphicon-circle-arrow-up")
	// 	else
	// 		$(this).attr('class',"glyphicon glyphicon-circle-arrow-down")

	// });


});