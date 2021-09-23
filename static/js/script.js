(function() {
    const search = document.location.search;
    const searchParamsString = search.substring(1);
    const searchParams = new URLSearchParams(searchParamsString);
    const searchElement = document.getElementById("search-div");
    const param1Value = searchParams.get('param1');

    console.log(searchParamsString)
    console.log(param1Value)
    console.log(searchElement)
    if (param1Value) {
      searchElement.innerHTML = param1Value;
    }
  })();
