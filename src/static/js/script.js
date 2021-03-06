

$(function(){
    $(".ui-draggable").hover(function(){
        $(this).css("background-color", "#12A191");
        }, function(){
        $(this).css("background-color", "#0E7F73");
    });
});

$(function() {
    $(".ui-draggable").draggable({
        cursor: "crosshair",
        revert: "invalid",

        helper : "clone"});

    $(".ui-droppable").droppable({
        accept: ".ui-draggable",
        drop: function(event, ui) {
            console.log(".ui-droppable");
            $( this ).find( ".ui-draggable" ).remove();
            var dropped = ui.draggable;
            var droppedOn = $(this);
            $(dropped).clone().css({top: 0,left: 0}).appendTo(droppedOn);
            var to_show = String($(ui.draggable).text().match(/\d{2}[:]\d{2}[:]\d{2}[,]\d{3}\s[-][-][>]\s\d{2}[:]\d{2}[:]\d{2}[,]\d{3}/g)[0])
            $( this ).find( "input" ).val(to_show)
        },

    });

});


submitForms = function(){
    document.forms["blueprint_sub_form"].submit();
    document.forms["base_sub_form"].submit();

}