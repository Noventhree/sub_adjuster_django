

$(function(){
    $("li").hover(function(){
        $(this).css("background-color", "pink");
        }, function(){
        $(this).css("background-color", "#89E8BF");
    });
});

//$(function() {
//    $(".ui-draggable").draggable({
//        cursor: "crosshair",
//        revert: "invalid",
//        helper : "clone"});
//
//    $(".ui-droppable").droppable({
//        accept: ".ui-draggable",
//        drop: function(event, ui) {
//            console.log(".ui-droppable");
//            $(".ui-droppable li").remove();
//            var dropped = ui.draggable;
//            var droppedOn = $(this);
//            $(dropped).clone().css({top: 0,left: 0}).appendTo(droppedOn);
//            var to_show = String($(ui.draggable).text().match(/\d{2}[:]\d{2}[:]\d{2}[,]\d{3}\s[-][-][>]\s\d{2}[:]\d{2}[:]\d{2}[,]\d{3}/g)[0])
//            document.getElementById('id_line_A').value=to_show
//        },
//
//    });
//
//});

//function getid(obj) {
//            alert(obj.id);
//        }
//var currentid = getid

submitForms = function(){
    document.forms["blueprint_sub_form"].submit();
    document.forms["base_sub_form"].submit();

}