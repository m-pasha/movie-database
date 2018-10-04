function oninit() {
    $('#searchMsg').hide();
    $('#resultMovie').hide();
}
function searchFilm() {
    title = $('#titleMovie').val();
    type = $('#typeMovie').val();
    year = $('#yearMovie').val();
    url = "http://www.omdbapi.com/?apikey=ebaf04d9&"+'&t='+title+'&y='+year+'&type='+type;
    $.ajax({
        type: "GET",
        url: url,
        dataType: "json",
        success: function (data) {
            if (data.Title) {
                $('#Title').text(data.Title);
                $('#Year').text(data.Year);
                $('#Actors').text(data.Actors);
                $('#Awards').text(data.Awards);
                $('#Country').text(data.Country);
                $('#DVD').text(data.DVD);
                $('#Director').text(data.Director);
                $('#Genre').text(data.Genre);
                $('#Plot').text(data.Plot);
                $('#Released').text(data.Released);
                $('#Runtime').text(data.Runtime);
                $('#Poster').attr("src", data.Poster);
                $('#searchMsg').hide();
                $('#resultMovie').show();
            } else {
                $('#searchMsg').show()
                $('#searchMsg').text(data.Error);
            }

        }
    });
}
function addFavourite() {
    console.log("Added")
}