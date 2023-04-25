$(document).ready(function(){
	$(".filter-checkbox,#priceFilterBtn").on('click',function(){
		var _filterObj={};
		$(".filter-checkbox").each(function(index,ele){
			var _filterVal=$(this).val();
			var _filterKey=$(this).data('filter');
			_filterObj[_filterKey]=Array.from(document.querySelectorAll('input[data-filter='+_filterKey+']:checked')).map(function(el){
			 	return el.value;
			});
		});

		// Run Ajax
		$.ajax({
			url:'/website/filter-data',
			data:_filterObj,
			dataType:'json',
			success:function(res){
				console.log(res);
				$("#filteredProducts").html(res.data);
			}
		});
	});
	// End

});

