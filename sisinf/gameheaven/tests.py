from django.test import TestCase
from gameheaven.models import Tienda, Consola, Videojuego, Trabajador, Administrador, Cliente, StockConsola, StockVideojuego, ReservaVideojuego, ReservaConsola
from gameheaven.DAOs import daoTienda, daoProductos, daoUsuario, daoReserva

# Create your tests here.

# Tests for DAOs
class TestDAOs(TestCase):
    def test_dao_tienda(TestCase):
        # Create
        tienda = Tienda(ciudad="Madrid", codigoPostal=28001)
        daoTienda.newTienda(tienda)
        # Read
        tienda2 = daoTienda.getTienda(tienda.id)
        assert tienda2.ciudad == tienda.ciudad
        assert tienda2.codigoPostal == tienda.codigoPostal
        # Update
        tienda2.ciudad = "Barcelona"
        daoTienda.updateTienda(tienda.id, tienda2)
        tienda3 = daoTienda.getTienda(tienda.id)
        assert tienda3.ciudad == tienda2.ciudad
        # Delete
        daoTienda.deleteTienda(tienda.id)
        try:
            tienda4 = daoTienda.getTienda(tienda.id)
            assert False
        except:
            assert True

    def test_dao_productos_consolas(TestCase):
        
        # Create
        consola = Consola(nombre="PS5", descripcion="La mejor consola del mercado", img="img/ps5.jpg", valoracion=4.5)
        daoProductos.newConsola(consola)
        producto = daoProductos.getConsola(consola.id)
        # Read
        producto2 = daoProductos.getConsola(producto.id)
        assert producto2.nombre == producto.nombre
        # Update
        producto2.nombre = "PS4"
        daoProductos.updateConsola(producto.id, producto2)
        producto3 = daoProductos.getConsola(producto.id)
        assert producto3.nombre == producto2.nombre
        # Delete
        daoProductos.deleteConsola(producto)
        try:
            producto4 = daoProductos.getConsola(producto.id)
            assert False
        except:
            assert True

    def test_dao_productos_videojuegos(TestCase):
            
            # Create
            videojuego = Videojuego(nombre="FIFA 21", descripcion="El mejor juego de fútbol", img="img/fifa21.jpg", valoracion=4.5, plataformas="PS5")
            daoProductos.newVideojuego(videojuego)
            producto = daoProductos.getVideojuego(videojuego.id)
            # Read
            producto2 = daoProductos.getVideojuego(producto.id)
            assert producto2.nombre == producto.nombre
            # Update
            producto2.nombre = "FIFA 20"
            daoProductos.updateVideojuego(producto.id, producto2)
            producto3 = daoProductos.getVideojuego(producto.id)
            assert producto3.nombre == producto2.nombre
            # Delete
            daoProductos.deleteVideojuego(producto)
            try:
                producto4 = daoProductos.getVideojuego(producto.id)
                assert False
            except:
                assert True
                
    def test_dao_usuario_trabajador(TestCase):  
            # Create
            tienda = Tienda(ciudad="Madrid", codigoPostal=28001)
            daoTienda.newTienda(tienda)
            admin = Administrador(email="admin@admin.com", password="admin", usuario="admin")
            daoUsuario.newAdministrador(admin)
            admin = daoUsuario.getAdministrador(admin.id)
            trabajador = Trabajador(email="test@test.com", password="test", usuario="test", idTienda=tienda, idAdmin=admin)
            daoUsuario.newTrajador(trabajador)
            # Read
            trabajador2 = daoUsuario.getTrabajador(trabajador.id)
            assert trabajador2.email == trabajador.email
            assert trabajador2.password == trabajador.password
            assert trabajador2.usuario == trabajador.usuario
            assert trabajador2.idTienda == trabajador.idTienda
            assert trabajador2.idAdmin == trabajador.idAdmin
            # Update
            trabajador2.email = "asdf@asdf.com"
            daoUsuario.updateTrabajador(trabajador.id, trabajador2)
            trabajador3 = daoUsuario.getTrabajador(trabajador.id)
            assert trabajador3.email == trabajador2.email
            # Delete
            daoUsuario.deleteTrabajador(trabajador)
            try:
                trabajador4 = daoUsuario.getTrabajador(trabajador.id)
                assert False
            except:
                assert True
            
    
    def test_dao_usuario_cliente(TestCase):
         # Create
            tienda = Tienda(ciudad="Madrid", codigoPostal=28001)
            daoTienda.newTienda(tienda)
            cliente = Cliente(email="test@test.com", password="test", usuario="test", idTienda=tienda)
            daoUsuario.newCliente(cliente)
            # Read
            cliente2 = daoUsuario.getCliente(cliente.id)
            assert cliente2.email == cliente.email
            assert cliente2.password == cliente.password
            assert cliente2.usuario == cliente.usuario
            assert cliente2.idTienda == cliente.idTienda
            # Update
            cliente2.email = "asdf@asdf.com"
            daoUsuario.updateCliente(cliente.id, cliente2)
            cliente3 = daoUsuario.getCliente(cliente.id)
            assert cliente3.email == cliente2.email
            # Delete
            daoUsuario.deleteCliente(cliente)
            try:
                cliente4 = daoUsuario.getCliente(cliente.id)
                assert False
            except:
                assert True
        

    def test_dao_usuario_admin(TestCase):
        admin = Administrador(email="admin@admin.com", password="admin", usuario="admin")
        daoUsuario.newAdministrador(admin)
        # Read
        admin2 = daoUsuario.getAdministrador(admin.id)
        assert admin2.email == admin.email
        assert admin2.password == admin.password
        assert admin2.usuario == admin.usuario
        # Update
        admin2.email = "admin2@admin2.com"
        daoUsuario.updateAdministrador(admin.id, admin2)
        admin3 = daoUsuario.getAdministrador(admin.id)
        assert admin3.email == admin2.email
        # Delete
        daoUsuario.deleteAdministrador(admin)
        try:
            admin4 = daoUsuario.getAdministrador(admin.id)
            assert False
        except:
            assert True

    def test_consola_tienda(self):
        tienda = Tienda(ciudad="Madrid", codigoPostal=28001)
        daoTienda.newTienda(tienda)
        consola = Consola(nombre="PS5", descripcion="La mejor consola del mercado", img="img/ps5.jpg", valoracion=4.5)
        daoProductos.newConsola(consola)
        daoTienda.addConsolaTienda(tienda, consola, 3, 3)        
        stock = daoTienda.getStockConsola(tienda.id, consola.id)
        assert stock.tienda == tienda.id
        assert stock.consola == consola.id
        assert stock.stock == 3
        assert stock.precio == 3
        daoTienda.removeConsolaTienda(tienda.id, consola.id)
        try:
            stock2 = daoTienda.getStockConsola(tienda.id, consola.id)
            assert False
        except:
            assert True

    def test_add_videojuego_tienda(TestCase):
        tienda = Tienda(ciudad="Madrid", codigoPostal=28001)
        daoTienda.newTienda(tienda)
        videojuego = Videojuego(nombre="FIFA 21", descripcion="El mejor juego de fútbol", img="img/fifa21.jpg", valoracion=4.5, plataformas="PS5")
        daoProductos.newVideojuego(videojuego)
        daoTienda.addVideojuegoTienda(tienda, videojuego, 3, 3)        
        stock = daoTienda.getStockVideojuego(tienda.id, videojuego.id)
        assert stock.tienda == tienda.id
        assert stock.videojuego == videojuego.id
        assert stock.stock == 3
        assert stock.precio == 3
        daoTienda.removeVideojuegoTienda(tienda.id, videojuego.id)
        try:
            stock2 = daoTienda.getStockVideojuego(stock.id)
            assert False
        except:
             assert True

    def test_reserva_consolas(TestCase):
        tienda = Tienda(ciudad="Madrid", codigoPostal=28001)
        daoTienda.newTienda(tienda)
        consola = Consola(nombre="PS5", descripcion="La mejor consola del mercado", img="img/ps5.jpg", valoracion=4.5)
        daoProductos.newConsola(consola)
        daoTienda.addConsolaTienda(tienda, consola, 3, 3)
        cliente = Cliente(email="alv@alv.com", password="alv", usuario="alv", idTienda=tienda)
        cliente2 = Cliente(email="jal@jal.com", password="jal", usuario="jal", idTienda=tienda)
        daoUsuario.newCliente(cliente)
        daoUsuario.newCliente(cliente2)
        reserva = ReservaConsola(cliente=cliente, consolaTienda=daoTienda.getStockConsola(tienda.id, consola.id), fecha="2020-12-12", estado="estadoNoCompletada")
        daoReserva.newReservaConsola(reserva)
        reserva2 = daoReserva.getReservaConsola(reserva.id)
        assert reserva2.cliente == cliente.id
        assert reserva2.consolaTienda_id == daoTienda.getStockConsola(tienda.id, consola.id).id
        assert 1 == daoReserva.filterReservasConsolaByTienda(tienda.id).count()
        daoReserva.updateClienteReservaConsola(reserva.id, cliente2.id)
        reserva55 = daoReserva.filterReservasConsolaByCliente(cliente2.id)
        
        assert reserva55[0].cliente.email == cliente2.email


        daoReserva.deleteReservaConsola(reserva.id)
        try:
            reserva3 = daoReserva.getReservaConsola(reserva.id)
            assert False
        except:
            assert True

    def test_reserva_videojuegos(TestCase):
        tienda = Tienda(ciudad="Madrid", codigoPostal=28001)
        daoTienda.newTienda(tienda)
        videojuego = Videojuego(nombre="starfield", descripcion="El mejor videojuego del mercado", img="img/stf.jpg", valoracion=4.5)
        daoProductos.newVideojuego(videojuego)
        daoTienda.addVideojuegoTienda(tienda, videojuego, 3, 3)
        cliente = Cliente(email="alv@alv.com", password="alv", usuario="alv", idTienda=tienda)
        cliente2 = Cliente(email="jal@jal.com", password="jal", usuario="jal", idTienda=tienda)
        daoUsuario.newCliente(cliente)
        daoUsuario.newCliente(cliente2)
        reserva = ReservaVideojuego(cliente=cliente, videojuegoTienda=daoTienda.getStockVideojuego(tienda.id, videojuego.id), fecha="2020-12-12", estado="estadoNoCompletada")
        daoReserva.newReservaVideojuego(reserva)
        reserva2 = daoReserva.getReservaVideojuego(reserva.id)
        assert reserva2.cliente == cliente.id
        assert reserva2.videojuegoTienda_id == daoTienda.getStockVideojuego(tienda.id, videojuego.id).id
        assert 1 == daoReserva.filterReservasVideojuegoByTienda(tienda.id).count()
        daoReserva.updateReservasVideojuegoCliente(reserva.id, cliente2.id)
        reserva55 = daoReserva.filterReservasVideojuegoByCliente(cliente2.id)
        
        assert reserva55[0].cliente.email == cliente2.email


        daoReserva.deleteReservasVideojuego(reserva.id)
        try:
            reserva3 = daoReserva.getReservaVideojuego(reserva.id)
            assert False
        except:
            assert True
             
