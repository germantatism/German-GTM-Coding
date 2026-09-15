# Palco + Yuno | Deep Dive — transcript 2026-09-15

**Recorded:** Sep 15, 2026 via Google Meet, 48 min (Fireflies)
**Yuno:** German Tatis (BDM NA), Carlos Andres Medina Rivas (Implementation Engineer), Joaquin Mann (BDM NA, se unió la semana anterior), Magdalena Torrealba Zozaya
**Palco:** Alfonso Uribarri (co-fundador, Madrid), Fernando Nava Feldman (Technical Account Manager, CDMX), Álvaro García Torres

## Resumen de lo que dijeron ellos (hechos, no inferencias)

- **Modelo de negocio (Alfonso):** las cuentas de procesamiento son de sus clientes (partners por país que conocen promotores y recintos). El cliente recauda y liquida mensualmente a Palco. Fee por ticket vendido, o precio fijo por evento según volumen. Los tickets son del cliente; Palco es la capa de tecnología. En el 99% de las operaciones actuales el dinero lo recibe el cliente (Fernando). Eventualmente quieren tener cuentas propias en México y Europa.
- **Interés principal (Fernando):** contar con las integraciones a métodos de pago sin construirlas ellos ("cuello de botella sumamente costoso").
- **Fricción principal (Alfonso):** el costo se traslada al cliente final; sus clientes escogen pasarelas por precio, no por seguridad. Esperan que el ahorro por ruteo compense el costo de Yuno.
- **Auto-configuración:** sus clientes configuran sus propias llaves; preguntaron si las credenciales se cargan solo por dashboard o también por API (Carlos: ambas, organization API con GET catálogo + POST conexión).
- **Split de pagos:** preguntaron por fee de comisión a una cuenta y precio del ticket a otra (Carlos: Split Marketplace en la petición de pago, sellers vía API, ejecuta el PSP que lo soporte).
- **On-sales:** pidieron panel de actividad global en tiempo real, no solo alertas por email (Carlos mostró Insights).
- **Integración:** Alfonso dijo que lo harían por SDK en el 90% de los casos; pidieron la documentación de SDK y API.
- **Dos modelos (German):** white label (fee fijo + variable por volumen) o solo conexión (solo variable). Alfonso: marca blanca con comercio propio de Palco para recintos grandes y clubes deportivos (clientes nuevos); a los proveedores locales actuales, que reciben el dinero directo, es difícil cambiarlos.
- **Pricing mencionado en la call:** German dijo "alrededor de quince mil dólares como fee mínimo" mensual; Alfonso asumió un rango de 15 a 30 mil mensual según volumen. German confirmó que a mayor volumen, menor costo por transacción.
- **Feedback de Alfonso:** "bastante logrado, fácil de configurar y bastante completo"; "me ha gustado bastante".
- **Siguientes pasos acordados:** acceso a sandbox (Fernando como usuario principal, copia a Alfonso y Álvaro), envío de documentación SDK y API, propuesta comercial la semana siguiente. Fernando pidió varias opciones de horario (viernes, lunes, martes) porque Patricio y quizás Miguel deben estar en la parte comercial.

## Transcript

0:00 | Fernando
Buenos días. German. Cómo estás?

0:02 | German
Fer. Fer. Muy bien. Muy bien. Y tú?

0:05 | Fernando
Todo muy bien. Gracias. Qué bueno.

0:10 | Alfonso
Hola. Qué tal? Buenos días.

0:12 | German
Mucho gusto. Cómo están?

0:15 | Alfonso
Bien. Muy bien. Qué?

0:18 | German
Bueno. Qué tal el fin de semana? Bien. Bien. Excelente. Hola. Cómo van? Mucho gusto. Buenos.

0:27 | Fernando
Días. Y este, qué tal? Buen día. Bueno, pues este, no sé si esperamos a alguien más de su lado.

0:38 | German
No. Ya con Charlie, estamos. Como les dije la semana pasada, la idea ahorita era como tomar un deep dive en el producto, revisarlo y buscar la manera de cómo andaríamos con todo el tema de la integración. También se suma Joaco. Joaco se unió al equipo la semana pasada. Entonces, ahí se los presento. La idea es que empiece como a sumarse a reuniones y ver cómo es el funcionamiento de todo.

1:13 | Joaquin
Hola. Hola. Muchas gracias.

1:16 | German
Y ahí por el acento, imagino que ya se dieron cuenta que es de su país.

1:22 | Alfonso
Ah, bien. Bueno. Muchas gracias. Sí, tenemos a Fernando, que también está por México y bueno, a Gordillo. Estamos en España. O sea, que tenemos. Bueno. Gracias.

1:35 | Joaquin
Por incluirme.

1:39 | German
Buenísimo. Equipo. Entonces, la idea para esta llamada, un poquito, es que arranquemos con un par de comentarios alrededor de su modelo de negocio, de cómo ustedes están monetizando de sus márgenes, que nos cuenten un poquito más, que hagamos como, de pronto, unos diez minuticos de Deep Dive en eso. Y luego ya pasamos a que Charly nos ayude con, con todo el tema de contarles frente a la integración. Ya entiendo que ustedes revisaron toda la documentación y tienen muy claro todo, pero ya el funcionamiento. Yo alcanzé a hablar con… con Uy. Se me escapa el nombre ahorita. Con Patricio. Con Patricio.

2:24 | Alfonso
Con.

2:25 | German
Patricio, la semana pasada, frente a, al tema de las credenciales y me, me confirmó que ustedes son dueños de las credenciales de sus clientes. Cierto?

2:36 | Alfonso
Bueno, a ver, realmente las cuentas suelen ser de nuestros clientes. Vale? Yo digo, de verdad que sí, que incluso, bueno, comentaste con Patricio, me lo comentó Fernando y un poco por comentaros el negocio. Realmente, nosotros operamos como ya sabéis, operamos en varios países, pero realmente las cuentas son de nuestros clientes. Vale? Ahora, aunque estamos yendo quizá a otro tipo de clientes, pues, como sabemos, hemos operado. Hasta el momento. Buscamos partner en cada uno de los países y esos partner, que son los dueños de la cuenta, son los que ya, incluso tienen contactos para, para el tema de ticketing, de vender entradas, que conocen, promotores, recintos y son los que se encargan de distribuir nuestro producto en, en cada uno de los países. Pero ese cliente es el propietario de la cuenta. Ese cliente es el que recauda y después, mensualmente nos hace a nosotros, pues, una transferencia, un ingreso, una liquidación. Y eso es como, como funcionamos hasta ahora. Es verdad que, bueno, no, no tuve la documentación, pero sí que es verdad que vi un poco la web, un poco para ver un poco cómo, cómo movís y cómo dedicabais. Entiendo que en este sentido, porque sí que es verdad que tenemos varias pasarelas, pero creo que una de las ventajas que sí, que ofrecéis y corregirme si me equivoco, es que vosotros podéis, de cierta forma, usar una. Pasarela u otra. Según. Las condiciones de la tarjeta y entiendo también de la tasa de intercambio que se va a procesar. O sea, que ahí se podría un poco jugar con cuál es más restrictiva en el caso de que a lo mejor os haya más riesgo o cuál me deja más margen de beneficio? En caso de que me deje menos riesgo. Ya digo, porque esta parte igual sí que habría que verla. Yo creo que entiendo que aquí se estudiarían, que entiendo que también estarás tú más al día en esto. Fernando. Sí que se estudiaría, por lo menos en los países donde pudiéramos, como, por ejemplo, pues, a lo mejor México, evidentemente, pues en Europa o sitios donde nos sea más fácil tener nosotros nuestras propias cuentas, que igual seamos nosotros ya, digamos, esos receptores del dinero, digamos, esa liquidación sea un poco al inverso.

4:33 | Fernando
Sí, digo, realmente, sí es eventualmente, un, un objetivo. Sin embargo, digamos, ahorita, y para, para ponerlo, digamos, muy, muy claro con el equipo. Yuno, digamos, el principal objetivo más allá de quién reciba el dinero o no recibe el dinero, que, en este caso, en el noventa y nueve por ciento de nuestras operaciones actuales, este es nuestro cliente. Realmente, digamos, lo que más nos interesa es la posibilidad de contar con las integraciones con los métodos de pago sin tener que trabajarlas nosotros.

5:08 | Alfonso
Claro. Sí.

5:09 | Fernando
Es un huello de botella sumamente, este, costoso y pues siempre. Sí.

5:17 | Alfonso
Claro. Aquí lo que sí, incluso tirando por ese hilo. Vale? Porque es verdad que claro, es o lo podéis imaginar, sobre todo, que cada vez que vamos a desembarcar en un país, cada país tiene sus pasajeras de pago, hay que implementarlas. Vamos. Lo que sí vemos aquí que entiendo que por eso os preguntaba el tema de que os funcionéis un poco como Bridge, en el que podéis variar el dinero y tener ese margen de beneficio. Porque entiendo que. Claro, el problema que también tienen nuestros clientes es que las pasarelas que buscan, muchas veces no son incluso, ni las más seguras, sino son las más baratas. Entonces, es verdad que si al final le damos unos costes más altos. Vale? Puede ser una barrera de entrada, aunque a nosotros nos simplifique la vida, porque es mucho más fácil entrar. Vale? Vemos que puede ser una barrera de entrada el que les aumente el coste a nuestro cliente final y al final decida no usar algo que no vendría bien a todos, porque al final sus costes son mayores. Vale? Pues eso era el tema de si esa rentabilidad realmente puede ser un atractivo para usar esta pasarela.

6:14 | German
Ok. Buenísimo. No, sin duda, es algo que podemos hacer al final del día. La idea según, lo que hablamos la semana pasada, es darles a ustedes todas las conexiones que nosotros tenemos para que luego ustedes las puedan ofrecer a sus clientes y sus clientes puedan usar el Smart Routing para incrementar sus tasas de operación. Obviamente, ganar ese poder de negociación que de pronto no tienen. Hoy en día, en el que agarran un procesador y les está cobrando por darte un número, quince centavos por transacción. Y hay un procesador dos que le dice, ven, si tú me mandas el tráfico a mí, te voy a cobrar once centavos por transacción. Entonces, ahí ganan ese poder de negociación y se dan a su cliente esa diferencia. Gracias.

7:06 | Alfonso
Una.

7:06 | German
Duda antes de empezar frente a cómo funciona todo. Y, obviamente, la idea es mostrarles el dashboard y tomar como una demo a profundidad y mostrarles un impacto real sobre cómo ayudamos nosotros a nuestros clientes a hacer eso. Decías ahorita que entonces, su cliente es el encargado de hacer el recaudo y luego sale y dispersa el dinero de regreso a ustedes. Ese, eso, como lo tienen estructurado, es como un fee por ticket que se vende, es un.

7:42 | Carlos
Depende.

7:43 | Alfonso
Del cliente del volumen. O sea, al final suele ser un fee por ticket. O a veces, si tienen un volumen, suele ser, incluso a lo mejor solo un evento. Es un precio fijo. Pero aún es verdad que hay diferentes modelos de negocio. Y.

7:56 | German
Ellos vienen siendo los dueños de los tickets? O los dueños de los tickets son ustedes. No?

8:00 | Alfonso
Los dueños de los tickets son ellos? Realmente. Nosotros solo prestamos el servicio.

8:03 | German
Claro. Ustedes son la capa de tecnología que les da a ellos la posibilidad de hacer el recaudo del dinero. Ok. Excelente. Buenísimo. No? Charlie. Entonces, si quieres, arranquemos con el dashboard. Entramos un poquito a mostrarles cómo funciona. Conectar diferentes procesadores. Obviamente, ahí van a encontrar herramientas antifraude que entiendo que es algo que les interesa. Muchísimo. Procesadores de pago y métodos de pago. También. Al final del día, nosotros tenemos integraciones directas con métodos de pago, pero también las tenemos, por poner un nombre, indirectas, en el sentido en el que ustedes van a tener acceso a todos los métodos de pago a la hora de ir conectándose con los diferentes procesadores…

8:59 | Carlos
Un momento. Super team. Bueno, bienvenido a todos. Me escuchan bien? Sí, sí. Vale. Listo. Entonces, bueno, como primera visual, este es el portal de entrada correspondiente al dashboard de Yuno. Aquí vamos a tener toda la configuración correspondiente a su, digamos, a su organización dentro de Yuno. Listo? Entonces, ustedes van a poder crear cuentas. Entonces, ustedes van a tener, digamos, su organización palco, pero dentro pueden crear subcuentas. Entonces, digamos que ustedes quieran dividir por cuentas, cada uno de los merchants que ustedes tienen asociados, pues pueden hacerlo así. Listo? Esa es una forma de hacer la división. Entonces, miren que ustedes aquí van a tener realmente la posibilidad de crear varias cuentas. Cada cuenta tiene un identificador único y justo ese identificador es el que ustedes van a asociar para enviar la transacción. Listo? O el procesamiento del pago. Algo interesante es que cada cuenta va a estar, digamos, va a tener su propia configuración de routing. Entonces, ustedes pueden, cada cuenta hacer esa configuración de. Listo. Si esta cuenta es para el merchant a, va a tener esta configuración de routing, cuenta b, lo mismo. Vale? Entonces, ahí ustedes pueden empezar a hacer como esa diferenciación, y es una forma un poco más sencilla de, tal vez de mantenerlo. No? Pueden tenerlo todo en uno, por supuesto. Pero es una forma. Gracias. Digamos que dentro de la configuración del dashboard, ustedes van. A poder crear sus propios perfiles. Nosotros tenemos por defecto unos perfiles, digamos, ya creados y establecidos. Ustedes pueden crear unos custom para entregar más o menos accesos a los dos ambientes, tanto a Sandbox como a producción. Entonces, los permisos están divididos y ustedes, digamos, que van a tener toda la autonomía para poder invitar a los usuarios, listo? A los que ustedes quieran como tal, pues, entregarles sus accesos y también qué usuarios van a poder acceder a qué cuentas. Pues cada cuenta va a tener también un cúmulo de usuarios que van a poder o no ver. Listo? Aquí, por ejemplo, les muestro todos los usuarios que hay creados en esta cuenta de pruebas que yo tengo. Entonces, aquí están los diferentes roles. Aquí pueden ustedes editarlo, desactivarlo, incluso, eliminar un usuario. Pueden descargarlo como para tener un control sobre los usuarios entre otra información. Incluso tenemos una sección de auditoría que quisiera mostrarles de una vez. Entonces, aquí en esta sección de auditoría va a permitir que ustedes vean qué usuario ha realizado, qué acción lo paso aquí a producción. Listo? Por ejemplo, aquí Carlos Medina. Joe hizo una configuración de una conexión. Listo? Entonces, aquí ustedes van a poder ver qué acciones hacen los diferentes usuarios. Vale? Entonces, ahí como que van a tener como esa visual completa. Vale? Si quieren, pasemos primero al tema de las conexiones. Entonces, aquí ustedes van a tener un catálogo con todos los proveedores, adquirentes. Bancos etcétera, que tenemos hoy disponibles en yuno Listo. Es. Un catálogo normal entonces. Por, ejemplo en, México Tenemos no, sé un, getnet Entonces. Ustedes, pueden buscar el proveedor que quieren conectar hacer, clic en connect Y. Aquí es donde nosotros vamos a solicitar esas credenciales para podernos conectar al proveedor es. Lo único que ustedes requieren configurar aquí en yuno Para? Nosotros puede? Ser la conexión con el proveedor listo. Es. Un poco la pregunta que se hacía germán si. Ustedes cuentan con esta información por. Supuesto para. Poderla configurar sí. Sí, contaríamos. Con esta información sí. Vale. Súper.

12:41 | Fernando
Pregunta.

12:41 | Carlos
Adelante. Este…

12:42 | Fernando
tema. De setup credentials Se. Tiene que hacer directamente por dashboard o? Se puede hacer también por api y? Te digo por, qué porque. Normalmente nuestros, clientes se autoconfiguran muchas. Veces nosotros no intervenimos en la configuración de las de, las es, decir ellos, ponen sus llaves no…

13:04 | Carlos
vale? Súper? Actualmente. Tenemos, las dos formas ustedes. Lo pueden configurar manual aquí en el dashboard o tenemos… un api que pueden usar también para hacer esta configuración un poco más automática aquí. Les muestro igual rapidito. Gracias.

13:25 | Carlos
Tenemos. La sección de organization entonces. Aquí, ustedes van a poder digamos, que en esta parte de organization ustedes, van a poder configurar vía api todo, esto que les estoy mostrando entonces. Miren, que aquí tenemos la parte de conexiones entonces. Ustedes, van a tener un get para obtener el catálogo completo de proveedores y así mismo saber, qué campos necesitan para la configuración y ya sería el post de crear conexión listo. Entonces? Ahí, lo pueden automatizar un poquito… listo. Ahí? Igual les podemos compartir esta documentación para para, que lo vayan checando sin teman… listo. Una? Vez ustedes crean la conexión van, a tener digamos, por, cada una de las cuentas que ustedes tengan creadas en yuno Van, a poder ver el listado de conexiones que ya tienen creadas entonces. Aquí, yo tengo todas estas que corresponden a conexiones de prueba y van a poder ustedes ver cómo es el listado que han configurado listo. Hay? Algo interesante que no les mostré que, hace parte como del smart routing que mencionaba germán y, es lo siguiente… esperen. Buscamos. Por, ejemplo en, Colombia Un, crianco yo. Aquí le doy el nombre… el, código en la terminal y acá hay una sección en la configuración que, es como setear los costos entonces. Se, pueden setear como esos costos de lo que cobra el procesador sí. Para? Poder hacer justo, ese análisis veo, que qué, procesador me está cobrando más. No, y? Eso se puede configurar a nivel del smart routing yo. Ahorita les muestro entonces. Aquí, les digamos, dependiendo, de lo que cada procesador psp adquiriente etcétera, digamos, cobre, se, puede configurar aquí listo, cuál? Es el costo por transacción exitosa y? En caso tal que cobre por transacción no exitosa se, puede configurar aquí el valor conceptual o el fijo y pues la, moneda que corresponda listo. Entonces? Eso, ayuda justo a hacer ese análisis… listo. Eso? Es como el catálogo de conexiones cada. Vez que ustedes crean una conexión en yuno O, sea hacen, la conexión con un proveedor de pago a, nivel del routing se, habilitan los medios de pago listo. Entonces? Aquí, tenemos también como una especie de catálogo pero, ya no hay conexiones sino, de medios de pago entonces. Aquí, por, ejemplo vemos, medio pago tarjeta, medios, de pago alternativos como, 711 En, México Adyen, Colombia. Wallets. Como, apple Pay, click to pay por. Ahí van, a ver ustedes paypal Mejor, dicho como, dependiendo, de la conexión los, medios de pago que se habilitan listo. Entonces? Si, entramos a tarjeta por, ejemplo aquí, ustedes van a tener una visual de las rutas las. Rutas también las pueden configurar vía api en, caso que lo requieran listo, pero? Aquí ya les muestro manualmente entonces. Algo, importante por, cambio de pago van, a tener siempre una ruta activa listo, las? Otras rutas que ustedes vayan teniendo digamos, que, vayan cambiando van, a quedarse archivadas es. Decir ustedes, pueden en, caso tal venir, revisar, qué había cambiado antes y volverla a publicar volverla, a usar etc, también. Hay una sección como de borrador en, la que ustedes pueden guardar una ruta entonces. Ustedes, crean su ruta pero, no la publican todavía entonces. La, van a tener ahí como en un espacio de borrador por si quieren luego usarla…

16:45 | Alfonso
sí. Porque. Los parámetros para ver esas rutas para. Poder marcar esas rutas bueno. No, sé si ya lo veremos ahora un.

16:53 | Carlos
Poco. Qué. Parámetros permite ah? Sí, como. Qué. Rutas tiene sí? Qué…

16:57 | Alfonso
parámetros. Permite fijar esas rutas…

16:59 | Carlos
sí. Está. Perfecto entonces. Si, yo creo una ruta… entonces, van a tener aquí como un lienzo en blanco vale. Vale? Perfecto… entonces. Aquí, este, es como su lienzo entonces. Por, defecto está, una condición y es todos los pagos hacia dónde van a ir ustedes. Pueden decir no todos. Los pagos de esta cuenta por, ejemplo se, van a procesar a través de un no, sé de, un cabinet… entonces. Esta, es la ruta más sencilla ahora. Ustedes, pueden empezar a agregarle condiciones entonces. Miren, que aquí hay una opción de añadir condición. Aquí. Ya se me despliega un cúmulo grande de justamente condiciones para yo poder enrutar mis pagos por diferentes proveedores o dependiendo de diferentes características entonces. Por, ejemplo ustedes, dicen no todo. Lo que son tarjetas por, ejemplo visa. Y mastercard Las… voy a enviar por el proveedor… vale. D? Local por, ejemplo… y. Miren que aquí yo ya empiezo a ver mis condiciones no. Si? Todo lo que entra de visa Y mastercard Todo, lo que llegue como visa Y mastercard Lo, voy a enviar por d local el. Resto lo voy a empezar a enviar por ged No. Esas? Son condiciones esas. Son condiciones perdón. Básicas. Ustedes, pueden crear tantas condiciones como quieran gracias, a la opción de metadata entonces. Ustedes, nos pueden enviar en la petición de pago metadata… es, decir un, aquí y un valor que ustedes quieran y. Pueden agregar nosotros. Decimos que ustedes tienen la posibilidad de agregar infinitas condiciones porque, la metadata básicamente es un montón de opciones listo, pues? Por, ejemplo aquí, no, sé cliente… preferente por, poner un ejemplo… sí, o no listo. Entonces? Miren, que va agregando condiciones… cómo. Hace este lienzo para determinar qué condición ir primero? Él? Revisa de arriba para abajo entonces. Él, va revisando de arriba hacia abajo digamos, una, a una si, no cumple con la condición baja y así hasta llegar a la última opción que, es all other payments listo.

19:14 | Carlos
Listo? No. Sé si hasta ahí tengan alguna pregunta…

19:16 | Alfonso
bien. Bien. Bien, va…

19:20 | Carlos
entonces. Aquí, es en donde ustedes pueden empezar a hacer como esa distribución de tráfico entonces. Digamos, que me voy por esta condición en, donde si, es un cliente preferente voy, a enviarlo por un camino puntual listo. Entonces? Aquí, yo añado lo…

19:32 | Alfonso
que. No es que eso sea en campo libre es. Que pasaremos en integración no. O? Sea al, final…

19:35 | Carlos
exactamente. Al. Crear el pago ustedes, pueden enviar esa metadata y aquí a, nivel de las rutas la, tenemos en cuenta y la leemos gracias. Bueno. Antes, de pasar a esto tal, vez mostrarles, qué otras condiciones tenemos por. Ejemplo tenemos, por bin si. Se hacen campañas ustedes, pueden hacer configuraciones por bin por, país por, dato adicional entonces. Por, ejemplo si, llegaran a ofrecer no, sé cuotas, entonces, ustedes, pueden aquí también redireccionar el tráfico dependiendo, de los installments listo. Entonces? Realmente, hay bastante hay. Bastantes campos que pueden usar para redireccionar el tráfico si. Es con cbb O sin cbb Por. Ejemplo no, sé un, tema de suscripciones no. Por? Montos que ustedes digan no. Un? Monto superior a mil dólares quiero, bueno, a, diez mil dólares quiero, pasarlo por, ejemplo por, una validación de tri diez entonces. Pueden, hacer una ruta que conlleve a eso voy. A hacerlo aquí rapidito solo, para mostrarles… y. Ves entonces. Por, ejemplo no, sé si son más de diez mil dólares… entonces. Yo, puedo decirle aquí pase esto por una autenticación tri diez… y. Si se aprueba la autenticación tri diez entonces, ahí, se envíala por el proveedor que corresponda… vale. Entonces? Ustedes, pueden ir haciendo rutas de este estilo bueno.

21:00 | Alfonso
Vale? Entiendo. He. Visto también que tenéis ahí los rechazos entiendo. Que tú puedes montar algo para si es rechazado por una pasarela lo. Interpretas con otra no. O? Sea para, pasarelas que tienen redirección eso, cómo se atiende al final salían las dos redirecciones internamente…

21:17 | Carlos
para? El tema de redirección por. Ejemplo para, un me, pago un ipm o me pago transferencia solamente. Serviría si hay un error o. Sea si, no se crea la redirección ahí. Sí ustedes, pueden hacer fallback a otro proveedor pero. Si se rechaza digamos, que en esos casos sí hay que empezar un nuevo proceso de compra por, lo que la persona ya se redirige una. Vez intenta hacer la compra regresa, al sitio tendría. Que volver a hacer un proceso de compra para volver a hacerlo listo…

21:45 | Alfonso
sí? Sí. No. Es. Que he visto que tenéis ahí el declinado digo. Pues, si había alguna forma de sí.

21:51 | Carlos
No. Este. Digamos, este, declinado es generalmente ya para tarjetas entonces. Ustedes, pueden configurar grupos de rechazo o si quieren reintentarlo todo entonces. Ustedes, pueden decir acá listo, voy, a todo lo que se rechaza reintentarlo, por no, sé un, pfizer… igual, pueden hacerlo con el error entonces. Miren, que aquí ambas rutas de rechazo y de error las proceso por un siguiente proveedor listo. Y?

22:15 | German
Hay. Un tema relevante a tener en cuenta es, que… la persona que está comprando el ticket no va a saber que d local rechazó que hubo un error o. Sea todo, va a pasar de manera tan automática que ahí nadie o, sea solamente, ustedes van a tener acceso a esa data…

22:37 | Alfonso
la. Que realmente fue rechazada inicialmente y luego la probó otro procesador…

22:43 | Carlos
claro. Sí. O. Sea ustedes, van a poder ver la ruta que tomó esa transacción y ver por qué pasó pero, el cliente final va a ver su digamos, su, estado final no… listo? Esto. A, nivel de fallbacks… quiero, mostrarles algo relacionado a como, la división de tráfico entonces. Por, ejemplo ustedes… tienen no, sé un, kuski Un, gannett… Entonces. Miren, que aquí él me dejó seleccionar en este paso dos probadores al. Mismo tiempo podemos. Seleccionar tres cuatro, etcétera, listo. Voy. A hacer el ejemplo con dos entonces. Aquí, ustedes pueden distribuir el tráfico entre… esos probadores que seleccionaron entonces. Por, ejemplo si, yo selecciono aquí que, se distribuya ochenta… pakushki Y veinte para gendet Ustedes, van a ver algo de este estilo entonces. Dependiendo, del flujo transaccional que empecemos a recibir vamos, a empezar a redistribuir el tráfico por uno y por otro vale. Esa? Es una forma de hacer split pero. También tenemos la sección del smart routing les. Voy a volver a hacer aquí el ejemplo… y. Bueno voy, a agregar un d local aquí. Ven tres… es. Esta parte de aquí entonces. El, smart routing les permite a ustedes optimizar un poco o. Sea optimizar, como ese flujo hacia qué proveedor enviarlo entonces. Ustedes, pueden optimizar por tasa de conversión y latencia o por tasa de conversión y costos cuando. Miramos los costos esa, configuración que. Vimos antes de colocar cuánto. Me cobra el proveedor aquí. Hace relevancia porque. Dependiendo de eso es, que él va a redistribuir el tráfico para que el costo sea el más bajo posible listo. Sí? Por. Ejemplo si, lo dejamos por tasa de conversión y latencia ustedes, pueden decir no, él, automáticamente digamos. Que nuestro sistema de inteligencia artificial maneja automáticamente el tráfico al cien por ciento entonces. Él, va a empezar a distribuir dependiendo, de justamente, esa, configuración tasa de conversión y latencia o, pueden hacerlo manual si. Es manual entonces. Ustedes, pueden decir listo, el, smart routing me controla el cincuenta por ciento del tráfico pero, yo quiero que a este proveedor se vaya tanto porcentaje a, este tanto, y a este tanto listo. Es? Lo que ustedes pueden configurar… y.

25:08 | Alfonso
Ahora. Te, voy a hacer un comentario tenéis. Pasarelas que tengan split de pagos porque? Nos ocurre mucho cuando el proveedor dice oye, yo, voy a vender un evento pero. La parte el, fee de la comisión de una cuenta el, precio del ticket para otra cuenta y. Eso muchas. Pasarelas de pago lo hacen con split de pagos eso. Lo tenéis contemplado eso. Es split De pagos se. Configuraría como una cuenta normal sí.

25:34 | Carlos
Se? Configuraría como una cuenta normal lo. Que pasa es que a nivel de cuando ustedes nos envían la transacción o el intento de pago hay, uno que es split Marketplace Entonces. Ahí, ustedes pueden definir es. Acá uno, de los en, este caso sería, de los sellers cuánto, flujo cuánto? Cuál, va a ser el dinero cuánto. Cuál, va a ser el fee etcétera, nosotros. Lo propagamos al proveedor al, psp que lo soporta y, finalmente ellos, son los que ejecutan el proceso no, de? Dispersión de fondos…

26:05 | Alfonso
sí. Vale. Vale.

26:08 | Carlos
Que. Incluso aquí ahí está la parte de sellers aquí. También en nuestra api les, muestro rapidito lo que está abajo… y ahí ustedes pueden gestionar esa parte aquí sellers entonces. Pueden, crear como los sellers pueden hacer onboarding también de quienes digamos, los, recipients del marketplace entonces. Quiénes, son los que van a dvd quiénes. Son los que van a recibir perdón esos, montos entonces? Eso, lo pueden hacer directamente desde el api vale. Listo? Entonces. Bueno, esa, es una también de las características que tenemos a nivel del smartroute gracias. Hay. Un punto interesante y es sobre monitores entonces. Miren, que todas las condiciones tienen como una campanita por. Ejemplo si, yo le activo aquí el monitor ustedes, pueden configurar aquí un umbral entonces. Por, ejemplo después, de cierto tiempo ya vemos que la tasa de aprobación es del ochenta y cinco por ciento les. Pongo un ejemplo… si. Llega a bajar por, ejemplo un, sesenta por ciento ustedes, pueden configurar una alerta pueden, configurar dos cosas alertas, y redistribución de tráfico entonces. Dependiendo, de la condición que ustedes elijan acá, ustedes, pueden decir listo, si, mi umbral baja tanto tanto, porcentaje envíe, un correo o, si tienen ustedes digamos, una, conexión a obscene pueden, activarla aquí para que reciban una llamada de forma automática…

27:40 | Alfonso
listo. Aquí.

27:43 | Carlos
Pueden. Configurar la cantidad de correos que quieran separados, por cómo pero, también pueden activar la redistribución de tráfico entonces. Qué, hace esto automáticamente? Dependiendo? De digamos, aquí, local está caído y todas las transacciones están entrando en error entonces. Nosotros, desde yuno Empezamos a redistribuir el tráfico para que ya no pasen por d local sino, por pfizer Es. Decir ya, no vamos a intentar por d local sino, por pfizer Va. A haber un flujo muy chiquitico que va a seguir intentando a d local para. Cuando se restablezca una. Vez vemos que se restablece el flujo vuelve, a estar como antes listo. Entonces? Esto, mejora latencias y pues permite, que finalmente la, transacción tengamos un intento mejor hacia… digamos, a, nivel de la tasa de aprobación listo. Entonces? Eso, es algo que ustedes también pueden configurar aquí a nivel de las rutas… eso. Sería como en, general la, configuración aquí de las rutas o del lienzo que ustedes pueden configurar digamos, a, su apotestad y, pues, diferenciado, por diferentes cuentas que ustedes creen en yuno… Algo. Que me sonaba german Tal, vez para mostrarles es que a nivel de proveedores no, solamente tenemos proveedores de pago sino, también tenemos soluciones antifraude por, ejemplo o, también soluciones tri dies va. Entonces? Como, que dentro del catálogo ustedes pueden encontrar todo este tipo de conexiones… bueno. Sí, y. No sé cómo vamos hasta ahí. Vale.

29:19 | Alfonso
Bien. Bien. Entiendo. Que cada uno con su coste ya. Digo. Aquí, el peligro sobre, todo porque, también luego os preguntaré digo, no, es tanto lo bueno que sea que. Es verdad que muchas veces para nosotros sí tiene mucho valor pero. Es verdad que el cliente muchas, veces cuando, el coste sube porque, eso a, veces muchas, veces dice en, una operación de este tipo no, puedes salir sin tres de ese y. El cliente dice ya pero. Es que me suben los costes y dice ya pero. Es que como empiezas a tener charva Tus, costes se van o. Sea sí. Entonces. Es, verdad que siempre tenemos mucha fricción con ese subir, costes vale. Por? Eso es un poco no. Sé me. Parece bien vale. Que. Al final un, poco lo dejas en manos del cliente oye. Si, tú quieres en, cuanto haya a, partir de un importe oye, tienes, que pasar por un cis ds tienes, que pasar por un sistema de scoring pero. Eso es verdad que a veces ir aumentando al final costes y. Es verdad que a nosotros nos costará un poco venderlo pero. Bueno ya, lo digo para, ser sincero me, parece que está bastante logrado fácil, de configurar y bastante completo… listo. Súper.

30:13 | Carlos
Bien. Va. Algo. Como para seguir… como complementando aquí el visual del dashboard dependiendo, de la integración que ustedes elijan tenemos. Aquí nosotros una configuración que es el checkout builder listo. Entonces? Nosotros, tenemos una integración sdk… como, varias versiones del sdk pero, el sdk básicamente, les, va a entregar a ustedes la visual de los medios de pago y el formulario va a estar soportado por yuno formulario para recibir los datos de tarjeta etcétera, etcétera, listo. Vemos? El otro pedazo que, es api entonces. Una, integración api es una integración directa server. To server ahí. Sí. Ya. Todo lo que es los campos de digamos, de, la información del cliente la, tarjeta y todo eso ya, eso es soportado por el merchant listo. Y? Hay que tener un nivel de pci como para tenerlo presente listo. Conceso? Vale.

31:15 | Alfonso
Sí? O. Sea de, pci comparing. Para poder eso vale.

31:20 | Carlos
Correcto. Con. El sdk no lo necesitan porque, nosotros somos quienes soportamos eso listo. Entonces? A, nivel del sdk ustedes, tienen aquí esta opción en el dashboard que, es el checkout builder ustedes. Aquí pueden activar y desactivar los medios de pago simplemente, con un click miren. Por, ejemplo aquí, yo quité tarjeta y quedó yapi Puedo, activar por aquí un 711 Puedo, activar un quest keep pay breve, fix pago, efectivo luego. Puedo quitar un apple Pay listo. Entonces? Esta, configuración se va a ver reflejada cuando ustedes inicialicen el checkout del lado de yuno… Entonces. Esto, les permite a ustedes también incluso, crear condiciones por. Ejemplo mostrar, ciertos medios de pago para ciertos lugares para, ciertos países etcétera, listo. Igual? Por, cuenta cada, cuenta va a tener su propio digamos, su, propia configuración de checkout pero, era como para que lo para, que vean un poco la facilidad de prender o apagar medios…

32:19 | Alfonso
de. Pago no. Pero? Incluso, es verdad que a veces tenemos cuentas pero, hay clientes nuestros, propios, clientes nuestros que, ese mismo cliente incluso opera en varios países incluso. Dependiendo de importes puede, ir por unas pasarelas o incluso o, sea es, verdad que incluso una misma cuenta puede usar estas configuraciones…

32:38 | Carlos
de. Acuerdo entonces. Ahí, con condiciones lo pueden hacer sin problema…

32:41 | Fernando
es. Por cuenta este, checkout…

32:44 | Carlos
no. Lo pueden hacer por cuenta lo, pueden hacer por cuenta y. De, todas formas también, tenemos una funcionalidad en la que para una misma cuenta ustedes pueden crear varios checkouts entonces. Miren, que aquí ustedes pueden crear digamos, aquí, tenemos el principal para la cuenta digamos, la, de carlos Medina Cierto, pero? Pueden crear un checkout también aparte para esa misma cuenta entonces. Si, bien pueden tener un checkout por cuenta también, pueden tener varios en la misma cuenta… y como lo requieran sin problema listo. Sí? Y. También tenemos como una sección de estilo esto. Lo pueden configurar también vía digamos, a, nivel de código pero, pues aquí está un poco esa configuración… también aquí a nivel del dashboard entonces. Ustedes, pueden decidir por, ejemplo si, quieren que se despliegue la información aquí mismo o, que se cree un modal por. Ejemplo en. El momento de seleccionar el medio de pago… cómo. Quieren ustedes mostrar los medios de pago por? Ejemplo express. Que, son los botones de paypal Google. Pay. Apple. Pay. Entre, otros y. Temas de un poco más como, estilo colores, la, letra etcétera, etcétera, listo. Que? Eso muchas veces sí se usa más a nivel de la conexión api es. Más sencillo es, como para que ustedes lo vean por acá. Vale. Eso? Como. A nivel general tenemos, toda una sección de operaciones aquí. En operaciones básicamente, ustedes, van a poder revisar descargar, reportes ver. Todas sus operaciones día a día vale. Un. Poco lo que mencionábamos ahorita de, ver cuáles son esos procesadores por los cuales intentó pasar un una, transacción… por. Ejemplo aquí. Yo, tengo un pago en Colombia Entonces. Miren, que aquí tenemos un como, una línea de tiempo ahí, que ustedes pueden ver la ruta que tomó paso por signify Que, es un motor antifraude y luego se fue por un procesador de pago…

34:47 | Alfonso
vale.

34:48 | Carlos
Entonces. Si, quieren verlo un poco más visual hay, un botoncito que es ver ruta y, aquí entramos al lienzo y él ilumina la ruta por la cual tomó la transacción… y. Entonces ustedes pueden tener un poco más de detalle vale.

35:04 | Alfonso
Y? Notaban en detalle paneles de actividad así, que no sea recibiendo alertas por email que, es un panel de actividad donde se puede ver datos por cuenta más, globales sobre. Todo a, lo mejor otro que tenemos mucho por, ejemplo son, on sale Vale. Y? Entonces en, periodos de tiempo muy cortos hay, como un volumen muy alto de pagos y generalmente se, suele estar monitorizando todo…

35:24 | Carlos
sí. Como. A nivel general me pregunta el consorcio sí. Sí.

35:28 | Alfonso
Como. A nivel general o. Sea que, se está probando un ochenta por ciento de las transacciones un, veinte por ciento se está redirigiendo no, sé a, getnet Un.

35:39 | Carlos
Ok. Ok. Tenemos. Una sección de insights que, es esta de arriba entonces. Este, ya mira como el overall de la cuenta no, entonces? Aquí, en la parte de overview entonces, ustedes, ya van a poder ver ok. Cuál. Es mi volumen de ventas por? Ejemplo diario, bueno. Tienen, varios filtros dependiendo. Del filtro él, va mostrando cantidad, de pagos aprobados ticket, promedio tasa, de conversión el. Volumen lo, aprobado o lo rechazado y. Tenemos una parte de volumen y tasa de conversión pues. Aquí ya vamos siendo un poquito más específicos en cuanto a los proveedores listo. Por. Ejemplo aquí, tenemos top proveedores por. Ejemplo aquí, tenemos tarjeta aquí, tenemos, workpay aquí. Ya agregamos uno los, países si, pasó por fraude tasa, de rechazo y top issuers no. Igual? Ustedes pueden llegar a agregar gráficos personalizados y. Alguno de estos que tenemos aquí establecidos digamos, no, les hace mucho sentido y. Por aquí tenemos un poco lo que usted mencionaba entonces. Por, ejemplo aquí, tenemos tasa de aprobación de tarjeta por proveedor entonces. Cuánto, por tu nota de spamming gateway, cuánto, por workpay y. En un primer intento cuál, es la tasa de aprobación y en un reintento cuánto, no Que? Ese reintento corresponde al fallback… entonces. Toda, esa información digamos, que la tenemos aquí en el insight a nivel general incluso, por condición entonces. Cada, condición tiene un id. Ustedes. Pueden darle un nombre y. Aquí también ustedes pueden ver la tasa de aprobación por condición no. A? Nivel del router… eso. Sería a nivel general…

37:17 | Alfonso
vale. Vale. Vale. Sí. Está. Bien vale. Incluso. Yo digo también, aprovechando, por ese miedo que tenemos a esa fricción nuestro, modelo de negocio que va por transacción o, sea coste, por transacción nuestros, costes que irían por transacción por, volumen…

37:37 | Carlos
los. Costos digamos, al, procesar la transacción sí.

37:41 | Alfonso
Digo. Vuestro, modelo de negocio cómo? Va vosotros? Cobráis? Por transacción cobráis? Por volumen por, o, sea por, volumen de importe por, número de operaciones un. Poco también por. Que luego os hay que trasladar a nuestro cliente final esos costes que, es lo que luego puede frenar más…

37:58 | Carlos
ya. Ok. Ok. Y. No sé german. Si, somos en el drive…

38:03 | German
perdón. Me. Confirma es? Que tengo el internet destruido…

38:07 | Alfonso
ah. Bien, bien, sí. Sí, sí. Que. Están preguntando un poco por vuestro modelo de negocio cómo. Cobráis o? Sea cobráis, por, transacción cobráis. Por, volumen de dinero procesado…

38:19 | German
ahí. Ahí y. Si me trago también, me avisa y. Te repito ahí, hay dos modelos posibles que estoy viendo frente a este caso y, es uno que ustedes utilicen en nuestra plataforma como un white Label En, el que le ofrezcan a sus clientes digamos, el, full equipo de lo que sería la plataforma de yuno Y. La otra la veo más como que ustedes simplemente se conecten a nosotros para tener acceso a todas las integraciones y obviamente, las, reglas de routing que hay detrás pero, ya dependería de ustedes y. Obviamente, cada, modelo funciona diferente el. Modelo del white label Funcionaría más como con un fee mijo Un, fee fijo y algo dependiendo, de los volúmenes transaccionales más, variable y. El otro ya sería únicamente en los volúmenes que ustedes procesen…

39:16 | Alfonso
claro. Entiendo. Que hay seguramente, si, nosotros agruparamos todos podríamos tener una mejor tasa porque, agruparíamos el grueso de todos los clientes y cada cliente por separado entiendo. Que seguramente la, tasa que o, sea le, podría dar un peor precio porque, claro, no, es lo mismo agrupar todos con un volumen mayor que a cada uno por separado o, eso daría igual más, o menos para el tema de costes… daría…

39:39 | German
igual. Al, final del día depende, o. Sea como, ustedes son quienes están procesando todo digamos. Que todo está pasando por palco y ahí nosotros vamos a tener visibilidad y todo entonces. Digamos, que en el dashboard como, lo veíamos ahorita tenemos, como el account grande que, vendría a ser palco y luego vamos a tener los subaccounts al. Final del día digamos. Que todo estaría bajo su scope entonces. Ya, depende obviamente, de, los volúmenes que ustedes procesen dentro de cada uno de sus clientes nosotros. No lo vamos a hacer con ninguno de sus clientes nosotros. Vamos a tener la relación con ustedes y…

40:16 | Alfonso
ustedes.

40:17 | German
Solamente. Van a tener que ir a donde sus clientes y decirles pues, darle, la opción de conectarse con quien ellos quieran conectarse…

40:27 | Alfonso
vale. Sí. Y. No sé si en esta semana o en otra no. Sé más, o menos cuáles son estos costes para saber cuánto puede incrementar un poco esas operaciones con respecto a lo que se…

40:37 | German
llama. La. Semana pasada hablamos de alrededor de quince mil dólares como nuestro fee mínimo pero. Bueno al, final del día depende de los productos de nosotros que ustedes quieran utilizar gracias. También. Obviamente. Los, volúmenes transaccionales al final del día entre, más volúmenes, muevan ustedes por nosotros menor, el, costo por transacción va a ser entonces, va, a haber mayor beneficio para ustedes vale.

41:02 | Alfonso
Ese? Volumen habláis de mensual de? Mensual vale. Vale. Sí. Que sería más o menos un coste mínimo de unos quince mil pero, sí que vendría a rondar no. Sé si es el coste mínimo vendría. A rondar seguramente. Pues, unos quince treinta más o menos mensual más. O menos por volumen que vale.

41:21 | German
Correcto. Vale.

41:23 | Alfonso
Y. Verdad que sí que. Bueno y. Habría que ver lo que se ahorra por el tema del rotamiento que, es donde esperamos nosotros hay. Que conseguir una tasa más baja dependiendo, de las reglas poder. Ver posiblemente, si tira por por, que en caso de Santander Te va a dar mejor tasa que si y. Te llevas al bbv las, de las, de banco o. Sea te, llevas a openpay O no sé si tenéis openpay O bancomer O lo que sea pues. Te llevas a las del bbv o lo que sea… vale. Vale. Si. Ya digo incluso, si nos podéis pasar esa documentación que, tenéis incluso, del appium que, si lo hiciéramos lo, haríamos por sdk vale. O? Sea el, noventa por ciento pero. Digo si, tuviese esa documentación del appium si, nos pudierais hacer llegar…

42:04 | Carlos
creo. Que sí ahí. Se las compartimos sin problema por correo vale.

42:08 | Alfonso
Incluso. Ya, digo esa, parte también la vemos un poco más con ya, con la parte más de negocio incluso. Le diríamos con pato Un poco para ver con nuestros clientes como se podría encajar para, que les fuera atractivo la oferta y ver un poco también donde podemos ahí ir apurando costes para sobre, todo con esa parte de enrutamiento que, es la que yo creo que podemos optimizar más… al. Final el, tema de seguridad también es importante ya, digo sobre, todo por importes y poder establecer el sistema de código poder, establecer el tdsq pero. Por, desgracia es, verdad que es algo que nuestros clientes suelen ser más abiertos al tema del pricing que al tema de la seguridad aunque, luego cuando, sufren los chatbots lo, sufrimos todos ahí…

42:51 | German
regresan. En serio…

42:53 | Carlos
de? Acuerdo sí. Ahí. Igual no, sé también, en nuestro lado podríamos darles un acceso a sandbox Al. Dashboard en sandbox Digamos, de, un ambiente de pruebas si. Ustedes quieren también, ir revisando y cacharreándole por ahí perfecto.

43:16 | Alfonso
El. Correo…

43:17 | Carlos
sería. El usuario principal y yo les envío la invitación mal…

43:21 | Alfonso
si. Quieres no, sé si que, te lo envían aquí fernando Y lo pones en copia a álvaro Y a mí también… fernando Estás muteado…

43:32 | German
sí. Sí, sin. Problema entonces. Pongo, aquí…

43:34 | Alfonso
vale. Pues. Si lo ponéis en copia a álvaro Y a mí que somos bueno, álvaro. Co y afuera com. Los. Dejo aquí todos para que los tengáis…

43:47 | German
de. Una avanzamos.

43:48 | Alfonso
Con.

43:49 | Carlos
Eso. El, día les llegaría el acceso equipo…

43:52 | German
una. Pregunta ahora. Frente, a lo que les propuso ahorita de, usar la solución como un white label o usar la solución como simplemente, para ustedes tener, acceso a todo y ofrecer qué. Sienten ustedes que les cierra mejor ahí? Pues?

44:11 | Alfonso
Para. Serte sincero es, verdad que ahora estamos yendo a otro tipo de clientes que, es incluso, a grandes recintos porque, es verdad que antes lo que buscábamos eran proveedores dentro del país entonces. Ellos, ahí es muy difícil decirle que no es en su propio comercio pero. Es verdad que sí que, sobre todo en grandes recintos o grandes eventos incluso, cruz Deportivos Sí, que estamos yendo directamente en. Esos casos es. Verdad que incluso para su facilidad es, verdad incluso. Clientes que a lo mejor no están técnicamente a, lo mejor no tienen tanta soltura si. Nosotros pudiéramos ir directamente con un comercio nuestro, sería una vía que podríamos estudiar y usar de marca blanca nosotros, y atenderlo todo a través de nuestro comercio…

44:48 | German
ok. Excelente. Ya. Digo…

44:50 | Alfonso
para. Clientes más grandes y proveedores locales no, va a ser muy difícil cambiarles sobre, todo porque, como están actuando así y reciben directamente el dinero va, a ser difícil cambiárselo pero. Sí que es verdad que sería algo que nos gustaría llevar a futuros clientes a, lo mejor de lo grande recién. Es otro tipo de eventos que son más pequeños pero… creo que iríamos a otro lugar vale. Perfecto. Vale. En. Principio no, sé si nos podéis ir mandando esto. Lo. Comentamos entiendo. Que bueno, yo, más o menos incluso, si hablaba un rato contigo yo, más o menos habría dado bastantes números ya. O. Sea que, a. Ver ya, digo, para, ser sincero ya, lo tenéis bastante bien atado y sobre todo eso de poder separar el tema de scoring el, tema de security o. Sea lo, paso o lo llevo a otras plataformas como, pfizer O lo que sea pues. Es verdad que está bien al. Final dice, que tengo más riesgo voy, por otro lado tengo, menos riesgo puedo, apurar la. Verdad es que…

45:44 | German
para. Ser…

45:45 | Joaquin
sincero. Me. Ha gustado bastante…

45:47 | German
no. Buenísimo. Ahí.

45:50 | Fernando
German. De su lado cuáles. Serían los siguientes pasos con nosotros y? Ahorita más allá del acceso al sandbox Y un poco más como para ir sabiendo que seguiría un poco más administrativo o hacia ver cómo podría ser la relación cuáles. Serían los siguientes pasos…

46:12 | German
sí? Claro, por. Supuesto ya. Nosotros tenemos la data que nos compartió patricio Frente, a sus volúmenes transaccionales ticket, promedio y todo entonces. Déjame, yo, organizo una propuesta comercial y. Qué tal si nos vemos la próxima semana iniciando, pronto lunes o martes a, esta misma hora y, ya la revisamos juntos…

46:36 | Fernando
ahí. Te pediría que nos mandes algunas opciones para porque. Ahí en la parte comercial es, necesario que esté por, lo menos patricio Seguramente, en, esta primera propuesta y. Quizás miguel Que, también estuvo la semana pasada un, momentito entonces. Y. Ahí sus agendas están un poco más apretadas normalmente entonces. Compárteme, algunas opciones de una vez que se puedan para, la próxima semana y yo intento ya coordinar con ellos entiendo. Que el objetivo de la sesión sería empezar a revisar pues, esta, primera propuesta comercial no…

47:15 | German
correcto? Ok.

47:18 | Fernando
Entiendo.

47:18 | German
Que. También hay cierta urgencia de su lado según. Me dijo patricio La semana pasada que, es un proyecto que queremos poner a andar lo más antes posible entonces. De, hecho si, quieren podemos, vernos este mismo viernes a, esta misma hora a, las diez de la mañana hora Colombia O, el lunes a las diez de la mañana hora Colombia…

47:42 | Fernando
Te. Pediría que me compartas las opciones y yo lo trato de cuadrar con con, patricio No. Sé si considero que miguel También tenga que estar pero, principalmente con ellos dos porque, para la parte comercial es indispensable que ellos estén en esa conversación entonces. Te, pediría ahí por, favor que, me compartas algunas opciones incluido. Viernes viernes, lunes, martes, para, poder cuadrar con ellos y en cuanto tenga una respuesta de ellos pues, confirmarte la fecha dale.

48:18 | German
Excelente. Listo. Entonces. Ahora, les comparto los horarios les, damos el acceso a sandbox Y les comparto también la documentación para que tengan acceso a todo…

48:32 | Fernando
perfecto.

48:34 | German
De. Una equipo. Muchas. Gracias nada.

48:37 | Fernando
Muchas. Gracias a. Vosotros…

48:38 | German
muchas. Gracias que. Estén bien…
