console.log(center)

function init(x, y) {
    let map = new ymaps.Map('separateMap598782829', {
        center: center,
        zoom: 15
    });

    let placemark = new ymaps.Placemark(center, {}, {

    });

    map.geoObjects.add(placemark);
}

ymaps.ready(init);
