importar  urllib2 , json

def  parseQuery ( q ):
	after_qmark  =  q [ 1 :]
	if ( len ( after_qmark ) <  2 ):
		retornar { }
	return  dict ([ p . split ( "=" ) para  p  em  q [ 1 :]. split ( "&" )])

def  build_querystring ( d ):
    retornar  '&' . join ([ '%s=%s'  % ( str ( k ), str ( v )) for  k , v  in  d . items ()])

def  json_http_call ( url , dados = Nenhum ):
    tente :
        se  os dados  forem  Nenhum :
            res  =  urllib2 . urlopen ( url )
        senão :
            res  =  urllib2 . urlopen ( url , dados )
        dados  =  res . leia ()
    exceto  urllib2 . HTTPError , e :
        dados  =  e . leia ()
        print  "erro na requisição: "  +  url  +  ": "  +  dados

    retorna  json . cargas ( dados )