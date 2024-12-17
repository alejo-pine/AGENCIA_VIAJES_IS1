from typing import List

from domain.entidades.excursion import Excursion
from domain.entidades.hotel import Hotel
from domain.entidades.vuelo import Vuelo


class PaqueteTuristico:
    def __init__(self, id: str, nombre: str, demanda: float = 0.0):
        self.id = id
        self.nombre = nombre
        self.precio = 0.0
        self.demanda = demanda
        self.vuelos: List[Vuelo] = []
        self.hoteles: List[Hotel] = []
        self.excursiones: List[Excursion] = []

    def calcular_precio(self) -> float:
        total = sum(vuelo.precio for vuelo in self.vuelos)
        total += sum(hotel.precio for hotel in self.hoteles)
        total += sum(excursion.precio for excursion in self.excursiones)
        self.precio = total
        return self.precio

    def ajustar_precio_demanda(self, demanda: float) -> None:
        self.precio += self.precio * (demanda / 100)

    def verificar_disponibilidad(self) -> bool:
        return all(vuelo.verificar_disponibilidad() for vuelo in self.vuelos) and \
               all(hotel.verificar_disponibilidad() for hotel in self.hoteles) and \
               all(excursion.verificar_disponibilidad() for excursion in self.excursiones)

    def agregar_vuelo(self, vuelo: Vuelo) -> None:
        self.vuelos.append(vuelo)

    def agregar_hotel(self, hotel: Hotel) -> None:
        self.hoteles.append(hotel)

    def agregar_excursion(self, excursion: Excursion) -> None:
        self.excursiones.append(excursion)

    def __repr__(self):
        return f"PaqueteTuristico({self.id}, {self.nombre}, Precio: {self.precio})"