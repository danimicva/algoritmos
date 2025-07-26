
from datetime import datetime
import statistics
from typing import List

from core import Estado, Mastermind
from resolvedores import ResolvedorBase


class PartidaTiempo():
    def __init__(self, partida, resolvedor, ms_resolucion):
        self.partida: Mastermind = partida
        self.resolvedor = resolvedor
        self.ms_resolucion = ms_resolucion


class EjecucionPartidas():
    
    def __init__(self, objetivos, caracteres, resolvedores, max_intentos, logger=None):
        self.objetivos = objetivos
        self.caracteres = caracteres
        self.resolvedores: List[ResolvedorBase] = resolvedores
        self.max_intentos = max_intentos
        self.partidas_resueltas: List[PartidaTiempo] = []
        self.partidas_no_resueltas: List[PartidaTiempo] = []
        self._logger = logger
        
    def ejecutar_partidas(self):
        for tipo_resolvedor in self.resolvedores:
            for o in self.objetivos:
                m = Mastermind(o, self.caracteres, self.max_intentos)
                instancia_resolvedor = tipo_resolvedor(partida=m, logger=self._logger)
                
                t_inicio = datetime.now()
                
                instancia_resolvedor.resolver()
                
                t_fin = datetime.now()
                pt = PartidaTiempo(m, instancia_resolvedor, (t_fin - t_inicio).total_seconds()*1000)
            
                if m.estado == Estado.FIN:
                    self.partidas_resueltas.append(pt)
                else:
                    self.partidas_no_resueltas.append(pt)
                    
                if self._logger:
                    fases = set(i.fase for i in m.intentos)
                    fases_intentos = ":".join(str(f)+":"+str(len([i for i in m.intentos if i.fase == f])) for f in fases)
                    self._logger.info("%s:%s:%s:%s:%s",
                                      tipo_resolvedor.nombre,
                                      self.caracteres,
                                      o,
                                      m.estado == Estado.FIN,
                                      fases_intentos)
    
    def _generar_estadisticas_valores(self, valores):
        if len(valores) == 0: 
            return "Sin datos"
        return (f"Máx: {max(valores)}. " +
            f"Mín: {min(valores)}. " +
            "Desv. est.: " + (f"{statistics.stdev(valores):.3f}. " if len(valores) > 1 else "Sin datos. ") +
            "Med: " + (f"{statistics.fmean(valores):.3f}. " if len(valores) > 1 else "Sin datos. "))
    
    
    def imprimir_info_estadistica(self):
        for r in self.resolvedores:
            partidas_resolvedor = [p for p in self.partidas_resueltas if type(p.resolvedor) == r]
            print(r.__name__)
            print(f" - Resueltas: {len(partidas_resolvedor)}/{len(self.objetivos)}.")
            print(f" - Nº intentos: {self._generar_estadisticas_valores([len(pt.partida.intentos) for pt in partidas_resolvedor])}")
            fases = [[i.fase for i in p.partida.intentos] for p in partidas_resolvedor]
            fases = set([item for lista in fases for item in lista])
            print(" - Fases:")
            for fase in fases:
                intentos_fase = [len([i for i in p.partida.intentos if i.fase == fase]) for p in partidas_resolvedor]
                print(f"   - {fase}: {self._generar_estadisticas_valores(intentos_fase)}")
            # print(f" - Tiempos: {self._generar_estadisticas_valores([pt.ms_resolucion for pt in self.partidas_resueltas])}")
