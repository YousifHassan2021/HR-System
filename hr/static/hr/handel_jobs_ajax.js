$(function (){
    var loadForm = function(){
            var btn = $(this);
            $.ajax({
                url :btn.attr("data-url") ,
                type:'get',
                dataType:'json',
                beforeSend:function(){
                    $('#edit_designation').modal("show");
                },
                success:function(data){
                    $("#edit_designation .modal-content").html(data.html_form);
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
                $('#edit_designation').modal("show");
            },
            success:function(data){
                $("#edit_designation .modal-content").html(data.html_form);
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
                    $("#jobs-table tbody").html(data.model_list);
                    $('#edit_designation').modal("hide");
                }
                else {
                    $("#edit_designation .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };
    
    // create
    $("#js-create").click(loadForm);
    $("#edit_designation").on("submit",".jobs_create_from",saveForm);

    // edit
    $("#jobs-table").on("click",".js-update",loadForm);
    $("#edit_designation").on("submit",".jobs_save_from",saveForm);


    // delete
    $("#jobs-table").on("click",".js-delete",loadForm);
    $("#edit_designation").on("submit",".jobs_delete_from",saveForm);

});

