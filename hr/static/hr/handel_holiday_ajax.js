$(function (){
    var loadForm = function(){
            var btn = $(this);
            $.ajax({
                url :btn.attr("data-url") ,
                type:'get',
                dataType:'json',
                beforeSend:function(){
                    $('#add_holiday').modal("show");
                },
                success:function(data){
                    $("#add_holiday .modal-content").html(data.html_form);
                }
            })
    };
    

    var saveForm = function(){
        var form = $(this);
        $.ajax({
            url: form.attr('action'),
            data:form.serialize(),
            type:form.attr('method'),
            dataType:'json',
            success: function (data){
                if(data.form_is_valid){
                    $("#holiday-table tbody").html(data.model_list);
                    $('#add_holiday').modal("hide");
                }
                else {
                    $("#add_holiday .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };

    // create
    $(".js-create").click(loadForm);
    $("#add_holiday").on("submit",".holiday_create_from",saveForm);
    
    // // edit
    // $("#promotion-table").on("click",".js-update",loadForm);
    // $("#add_promotion").on("submit",".promotion_save_from",saveForm);

    // delete
    $("#holiday-table").on("click",".js-delete",loadForm);
    $("#add_holiday").on("submit",".holiday_delete_from",saveForm);

});

