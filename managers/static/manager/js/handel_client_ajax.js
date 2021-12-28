$(function (){
    var loadForm = function(){
            var btn = $(this);
            $.ajax({
                url :btn.attr("data-url") ,
                type:'get',
                dataType:'json',
                beforeSend:function(){
                    $('#add_client').modal("show");
                },
                success:function(data){
                    $("#add_client .modal-content").html(data.html_form);
                }
            })
    };
    

    $(".js-create").click(function(){
        var btn = $(this);
        $.ajax({
            url:btn.attr("data-url"),
            type:'get',
            dataType:'json',
            beforeSend:function(){
                $('#add_client').modal("show");
            },
            success:function(data){
                $("#add_client .modal-content").html(data.html_form);
            }
        })
    })


    var saveForm = function(){
        var form = $(this);
        $.ajax({
            url: form.attr('action'),
            data:form.serialize(),
            type:form.attr('method'),
            dataType:'json',
            success: function (data){
                if(data.form_is_valid){
                    $("#client-table tbody").html(data.model_list);
                    $('#add_client').modal("hide");
                }
                else {
                    $("#add_client .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };
    
    // create
    $(".js-create").click(loadForm);
    $("#add_client").on("submit",".client_create_from",saveForm);

    // edit
    $("#client-table").on("click",".js-update",loadForm);
    $("#add_client").on("submit",".client_save_from",saveForm);


    // delete
    $("#client-table").on("click",".js-delete",loadForm);
    $("#add_client").on("submit",".client_delete_from",saveForm);

});

