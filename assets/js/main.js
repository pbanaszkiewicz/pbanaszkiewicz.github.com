// resetting
var last_txt = $("#searchinput").val();

function react_on_change(e) {
    if ($(e.target).val() != last_txt)
    {
        $("#searchinput").tooltip("hide");
        $("#searchinputgroup").removeClass("error success");
        last_txt = $("#searchinput").val();

        $("#search_results").addClass("hidden");
    }
};

$("#searchinput").keyup(function(e) {
    react_on_change(e);
});

function show_results(ids, keyword) {
    $("#search_results").html("");

    $(ids).each(function(index, element) {
        $("<h6>")
            .html(
                  $("<a>")
                    .attr("href", search.lookup[element][0])
                    .html(search.lookup[element][1])
                 )
            .appendTo("#search_results");

        $("<p>")
            .html(
                  $("<small>").html("…" + search.context(keyword, element, 1)
                                    + "…")
                 )
            .appendTo("#search_results");
    });

    $("#search_results").removeClass("hidden");
};

$("#searchform").submit(function() {
    var rv;
    var keyword = $("#searchinput").val();
    rv = search(keyword);
    console.log(rv);

    if (typeof rv != "undefined")
    {
        var results_ids = Array();
        $(rv).each(function(index) {
            $(rv[index]).each(function(index2) {
                results_ids.push(rv[index][index2]);
            })
        })
        // console.log(search.context(keyword, rv[1][index], 2));
        console.log(results_ids);
        console.log($.unique(results_ids));
        // console.log(search.lookup[results_ids[0]]);

        $("#searchinputgroup").addClass("success");

        show_results(results_ids, keyword);
    }
    else
    {
        $("#searchinputgroup").addClass("error");
        $("#searchinput").tooltip("show");
    }

    return false;
});

