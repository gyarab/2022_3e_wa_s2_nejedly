

var center = document.createElement('center');

var table = document.createElement('table');

for (let index = 0; index < 8; index++) {
    var tr = document.createElement('tr');
    for (let j = 0; j < 8; j++) {
        var td = document.createElement('td');
        if((index+j) % 2 == 0) {
                td.setAttribute('class', 'square square_white');
                tr.appendChild(td);
        } else {
            td.setAttribute('class', 'square square_black');
            tr.appendChild(td);
        }
    }
    table.appendChild(tr);
}
center.appendChild(table);
table.setAttribute('cellspacing', '0');
document.body.appendChild(center);