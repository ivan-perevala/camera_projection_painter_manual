Import Scene
############

Stage :doc:`setting up the context <setup-context>` as well as an independent operator. In fact, it's just a wrapper for standard import operators with presets.

If the presets are not suitable for any reason, you can always import the scene manually and skip this stage when setting up the context - just do not select any file.

So, in order to use this operator, you need to select a file to import and select the default settings for :ref:`third-party <Software>` files. This setting is saved as addon preference so you can do it once.

.. note::

    The current version of the addon only has presets for **Reality Capture**. It is obvious that we plan to expand the support of files of third-party software.

Next, the file type will be automatically determined using its extension. Files supported by the current version of the addon:

* ``Wavefront (.obj)``, ``Collada (.dae)`` - used built-in Blender importers.
* ``Autodesk (*.fbx)`` - the standard FBX file import addon will be used, so it should be enabled.

If these requirements are not met, the files will be hidden in the file manager and refused import. However, this is more information for users who use their own Blender builds.


.. Стадія :doc:`налаштування контексту <setup-context>` а також самостійний оператор. Фактично, це лише обгортка для стандартних операторів імпорту з попередніми налаштуваннями.

.. Якщо попередні налаштування з будь-яких причин не підходять, завжди можна імпортувати сцену вручну і під час налаштування контексту пропустити виконання цієї стадії - для цього потрібно просто не обрати жодного файлу.

.. Отже, для того аби скористатися цим оператором необхідно обрати файл для імпорту і обрати попередні налаштування для файлів :ref:`сторонніх програм <Software>`. Ці налаштування зберігаються як користувацькі налаштування доповнення тому можна зробити це один раз.

.. .. note::

..     Поточна версія доповнення має лише попередні налаштування для **Reality Capture**. Очевидно що плануємо розширити підтримку файлів сторонніх програм.

.. Далі буде автоматично визначено тип файлу використовуючи його розширення. Файли які підтримує поточна версія доповнення:

.. ``Wavefront (.obj)``, ``Collada (.dae)`` - використовуються вбудовані імпортери Blender.
.. ``Autodesk (*.fbx)`` - буде використано стандартне доповнення імпорту FBX файлів, тому воно повинно бути увімкнено.

..  Якщо ці вимоги не виконано то файли буде приховано в файловому менеджері і відмовлено в імпорті. Втім, це інформація більше для користувачів що використовують власні збірки Blender.