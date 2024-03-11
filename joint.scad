// Модель соединения в виде цилиндра и сферы

// Перемещение
translation = [0, 0, 10];

// Вращение
rotation = [0, 0, 0];

// Радиус соединения
linkRadius = 1;

// Радиус шарнира
jointRadius = 2;

// Качество
$fn = 36;

// Отладка
debug = true;

// Модуль соединения (вдоль оси z)
module joint(l = norm(translation), r1 = linkRadius, r2 = jointRadius)
{
    cylinder(l, r1, r1);
    translate([0, 0, l]) sphere(r2);
};

// Модуль базиса
module basis(l = 10 * linkRadius, r1 = linkRadius / 3)
{
    color("red") rotate([0, 90, 0]) cylinder(l, r1, r1);
    color("green") rotate([-90, 0, 0]) cylinder(l, r1, r1);
    color("blue") cylinder(l, r1, r1);
}

// Бинормаль к двум векторам
function binormal(v1, v2) = cross(v1, v2);

// Угол между двумя векторами
function angle(v1, v2) = acos((v1 / norm(v1)) * (v2 / norm(v2)));

// Соединение
rotate(angle(translation, [0, 0, 1]), binormal([0, 0, 1], translation)) joint();

// Базис (в режиме отладки)
if (debug) translate(translation) rotate(rotation) basis();
