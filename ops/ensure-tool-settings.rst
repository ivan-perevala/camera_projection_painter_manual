Ensure Tool Settings
####################

The last stage of setting up the work context (:doc:`setup-context`).

First, the availability of the drawing object will be checked. The active object must be a mesh with at least one polygon and an active UV map. If such an object is not available, the first visible scene object that matches these parameters will be selected. At the end of this check, the following options are possible:

* Object found - execution will continue.
* The object is found, but it has no polygons - a message about this will be reported and execution will be interrupted.
* The object is found, it has at least one polygon, but there is no active UV map - execution will continue, but in a limited mode - such a message will be reported. Obviously, editing the canvas in this case will not work, but this mode of operation can be useful if, for example, you only need to change the parameters of certain cameras and export camera data back to third-party software.

If the execution continues, then the tool and the scene will be set up. This section can be used to understand how you can set up a work context manually:

* The work mode will be changed to texture paint.
* The Clone tool will be selected.
* Texture drawing mode will be changed to "Single Image".
* The use of the clone layer will be enabled.

At the end of the execution, the operator will change the lighting type in all viewers of the current program window to flat - this way of displaying the object is best suited for editing textures.

Next, the main workflow of the add-on will be launched - it is important that there is at least one camera in the scene, even if it is inactive. During work, the main operator will independently ensure that an active camera is set - it is from it that the projection will take place.

.. Остання стадія налаштування контексту роботи (:doc:`setup-context`).

.. Спершу відбудеться перевірка наявності об'єкту для малювання. Активний об'єкт повинен бути сіткою, принаймні з одним полігоном і активною UV мапою. Якщо такий об'єкт відсутній то буде обрано перший з видимих об'єктів сцени що відповідають цим параметрам. Наприкінці цієї перевірки можливі такі варіанти:

.. * Об'єкт знайдено - відбудеться продовження виконання.
.. * Об'єкт знайдено, але у нього відсутні полігони - буде висвітлено повідомлення про це і виконання буде перервано.
.. * Об'єкт знайдено, в нього є принаймні один полігон, але відсутня активна UV мапа - виконання буде продовжено, але у обмеженому режимі - таке буде висвітлено повідомлення. Очевидно що редагувати полотно у такому разі не вийде, але цей режим роботи може бути корисним якщо наприклад, потрібно лише змінити параметри певних камер і експортувати дані камер назад до стороннього програмного забезпечення.

.. У разі продовження виконання далі відбудеться налаштування інструментів і сцени. Ця секція може бути використана щоб розуміти як можна налаштувати контекст роботи вручну:
.. * Режим роботи буде змінено на малювання текстури.
.. * Буде обрано інструмент "Клонування".
.. * Режим малювання текстури буде змінено на "Одне Зображення".
.. * Буде ввімкнено використання шару клонування.

.. Наприкінці виконання оператор змінить тип освітлення у всіх переглядачах поточного вікна програми на пласке - цей спосіб відображення об'єкту найкраще підходить для редагування текстур.

.. Далі відбудеться запуск основного робочого процесу доповнення - важливо аби у сцені була принаймні одна камера, навіть неактивна. Основний оператор під час роботи самостійно буде слідкувати щоб була встановлена активна камера - саме з неї буде відбуватися проекція.