var taskId = 

    $.ajax({
        url: '/api/crawl/',
        type: 'GET',
        success: console.log('good'),
        error: console.log('not'),
    })

  function checkCrawlStatus(taskId){
        $.ajax({
            url: '/api/crawl/?task_id='+taskId+'/',
            type: 'GET',
            success: console.log('good'),
            error: console.log('not'),
        })
    }

function crawlSuccess(data){
    taskId = data.task;
    //uniqueId = data.unique_id;
    statusInterval = setInterval(function() {checkCrawlStatus(taskId);}, 2000);
}

function crawlFail(data){
    $('#progress').html(data.responseJSON.error);
    $('#progress').attr("class", "alert alert-danger");
}
