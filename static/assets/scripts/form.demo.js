(function($) {
	"use strict";

	// Date Picker

	if ($("#datepicker").length)
		$('#datepicker').datepicker({
			autoclose: true,
			todayHighlight: true,
			format: "dd/mm/yyyy",
			language: 'pt-BR'
		});

})(jQuery);