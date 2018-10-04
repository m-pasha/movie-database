function oninit() {
    $('#searchMsg').hide();
    $('#resultMovie').hide();
    $('#addedMovie').hide();
}
function searchFilm() {
    $('#addedMovie').hide();
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
                $('#resultMovie').hide();
                $('#searchMsg').show()
                $('#searchMsg').text(data.Error);
            }

        }
    });
}
function addFavourite() {

    data_movie = {
        "title": $('#Title').text(),
        "year": $('#Year').text(),
        "actors": $('#Actors').text(),
        "awards": $('#Awards').text(),
        "country": $('#Country').text(),
        "dvd": $('#DVD').text(),
        "director": $('#Director').text(),
        "genre": $('#Genre').text(),
        "plot": $('#Plot').text(),
        "released": $('#Released').text(),
        "runtime": $('#Runtime').text(),
        "poster": $('#Poster').attr("src")
    }

    $.ajax({
        type: "POST",
        url: "/favourite/",
        data: JSON.stringify(data_movie),
        contentType: "application/json",
        dataType: "json",

        complete:(function() {
            $('#addedMovie').show();
            })
    });
}