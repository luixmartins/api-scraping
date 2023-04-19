import managedb

class Filter():
    def __init__(self) -> None:
        self.clima = ['aptidão climática','bioclima','clima alpino','clima antártico','clima árctico',
                        'clima árido','clima continental','clima de deserto','clima de monção','clima de montanha',
                        'clima de litoral','clima equatorial','clima húmido','clima mediterrânico','clima no seio de uma cultura',
                        'clima oceânico','clima polar','clima seco','clima semiárido','clima semi-húmido','clima sub-húmido',
                        'clima subtropical','clima temperado','clima tropical','condição meteorológica','fitoclima',
                        'macroclima','mesoclima','microclima','paleoclima','tempo meteorológico','zona climática','zoneamento climático',
                        'climate fitness','bioclimate','alpine climate','antarctic climate','arctic climate','arid climate','continental climate',
                        'desert climate','monsoon climate','mountain climate','coastal climate','equatorial climate',
                        'humid climate','mediterranean climate','climate within a culture','oceanic climate','polar climate','dry climate','semi-arid climate','semi-humid climate','sub-humid climate',
                        'subtropical climate','temperate climate','tropical climate','weather condition','phytoclimate',
                        'macroclimate','mesoclimate','microclimate','paleoclimate','weather weather','climate zone','climate zoning'
                    ]
        self.politica = ['controle governamental','estratégia de desenvolvimento','intervenção estatal','intervenção governamental',
                            'política administrativa','política agrícola','política alimentar','política ambiental','política comercial',
                            'política crédito','política de desenvolvimento','política de energia','política de estruturas',
                            'política de investigação','política de pesca','política de pesquisa','política de preços','política de produção',
                            'política de tributação','política econômica','política educacional','política financeira','política fiscal',
                            'política florestal','política governamental','política industrial','política monetária','política nacional',
                            'política regional','política social','política públicas','reforma',
                            'government control','development strategy','state intervention','government intervention',
                            'administrative policy','agricultural policy','food policy','environmental policy','commercial policy',
                            'credit policy','development policy','energy policy','structures policy',
                            'research policy','fishing policy','research policy','price policy','production policy',
                            'taxation policy','economic policy','educational policy','financial policy','tax policy',
                            'forestry policy','government policy','industrial policy','monetary policy','national policy',
                            'regional policy','social policy','public policy','reform'
                    ]
        self.animal = ['alimentação na seca','alimentação suplementar','arraçoamento','desmama','engorda','pastagem',
                        'dry feeding','supplementary feeding','racking','weaning','fattening','pasture'
                    ]
        self.exportacao = ['comércio externo','comércio internacional','balança de pagamentos','cadeia produtiva','corredor de exportação',
                            'cadeia produtiva','foreign trade','international trade','balance of payments','productive chain','export corridor',
                            'productive chain'
                        ]
        self.transporte = ['aviação','sistema de carga unitarizada','tráfego','transporte aéreo','transporte de animais',
                            'transporte em contentor','transporte ferroviário','transporte fluvial','transporte frigorífico',
                            'transporte marítimo','transporte por água','transporte rodoviário',
                            'aviation','unitary cargo system','traffic','air transport','animal transport',
                            'container transport','rail transport','river transport','refrigerated transport',
                            'maritime transport','water transport','road transport'
                        ]
        self.doencas = ['ácaro nocivo','ácaro prejudicial','insecto prejudicial','peste dos animais','planta nociva',
                            'praga das plantas','praga animal','praga planta','praga de produto armazenados','praga exótica',
                            'praga florestal','praga migratória','praga quarentenária','roedor',
                            'harmful mite','harmful mite','harmful insect','animal pest','harmful plant',
                            'plant pest','animal pest','plant pest','stored product pest','exotic pest',
                            'forest pest','migratory pest','quarantine pest','rodent'
                    ]
        
    def check_terms(self, id_news, text):

        text = text[0][0]
        for politica in self.politica:
            if politica in text.lower():
                managedb.insert_terms(id_news, 1)

        for clima in self.clima:
            if clima in text.lower():
                managedb.insert_terms(id_news, 2)
        
        for exportacao in self.exportacao:
            if exportacao in text.lower():
                managedb.insert_terms(id_news, 3)
        
        for animal in self.animal:
            if animal in text.lower():
                managedb.insert_terms(id_news, 4)
        
        for transporte in self.transporte:
            if transporte in text.lower():
                managedb.insert_terms(id_news, 5)
        
        for doencas in self.doencas:
            if doencas in text.lower():
                managedb.insert_terms(id_news, 6)
