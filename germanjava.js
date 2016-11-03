

<script>
function myFunction() {
     // Make a get request to grab URLs
    var ajax = $.ajax('/api/songs', {
        type: 'GET',
        dataType: 'json'
    });
    ajax.done(this.onGetSongsDone.bind(this));
    ajax.fail(this.onFail.bind(this, "Getting song information"));
};
}
</script>

