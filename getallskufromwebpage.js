var dataIds = $x('//div[@data-id]/@data-id');
dataIds.forEach(function(dataId) {
    console.log(dataId.value);
});


// exporting directly to csv
// Select all div elements with data-id attribute
var divsWithDataId = document.querySelectorAll('div[data-id]');

var csvContent = "data-id\n";

divsWithDataId.forEach(function(div) {
    var dataIdValue = div.getAttribute('data-id');
    csvContent += dataIdValue + "\n";
});

var blob = new Blob([csvContent], { type: 'text/csv' });

var link = document.createElement('a');
link.href = window.URL.createObjectURL(blob);
link.download = 'data_ids.csv';

link.click();
