from models.cryptography import Cryptography
# Supongamos que contrasena_en_db es la contraseña encriptada almacenada en la base de datos
contrasena_en_db = "qZzK8+0KAsn6slbzoOR2D6yQ4G5j9vGeG34L1nGLMcB/tRUaGA=="

# Instanciamos la clase Cryptography
cryptography = Cryptography()

# Desencriptamos la contraseña almacenada en la base de datos
contrasena_desencriptada = cryptography.decrypt_data(contrasena_en_db)

print("Contraseña desencriptada:", contrasena_desencriptada)
