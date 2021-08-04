(function($) {
	"use strict";

	// Date Picker

	if ($("#datepicker-autoclose").length)
		$('#datepicker-autoclose').datepicker({
			autoclose: true,
			todayHighlight: true,
			format: "mm/dd/yyyy",
			language: 'pt-BR'
		});

})(jQuery);