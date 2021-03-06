import requests
import time
from flask import Flask
from twilio.rest import Client
from get_token_ticker import get_token
from place_new_order import place_order
# baseUrl = 'https://api.latoken.com'
# endpoint = '/v2/ticker'
# url = baseUrl + endpoint

# response = requests.get(url)
# json_response = response.json()
# json_length = len(json_response)
# Write-Overwrites
# file1 = open("json_tokens.txt","w")#write mode
# file1.write(str(json_response))
# file1.close()

# list_o = []
# for i in json_response:
#     list_o.append(i['tag'])

#print(list_o)




list_all_token = ["ORE/USDT","OCB/ETH","KEY/USDT","NAUSICAA/USDT","NKN/BTC","AMPL/USDT","NFTS/USDT","HTL/BTC","HNT/USDT","CLU/USDT","XLAB/USDT","HITX/USDT","DAO/USDT","LBY/USDT","SEG/USDT","WGL/USDT","BEER/USDT","EFK/USDT","SAND/USDT","WAR/BTC","CHZ/USDT","CYS/USDT","SHIH/USDT","XEM/BTC","ANKR/USDT","YFI/BTC","DUKE/USDT","AGN/USDT","SPY/USDT","GHD/USDT","RLC/ETH","FAN/USDT","EVCOIN/USDT","STORJ/USDT","AION/BTC","REAP/USDT","CTC2/USDT","VTHO/USDT","CATGIRL/USDT","AG10/USDT","AAVE/USDT","LEDU/BTC","SPG/USDT","SACOI/ETH","GXT/BTC","SAFEMARS/USDT","BSP/USDT","TRX/USDT","RBUNNY/USDT","NYT/USDT","REQ/USDT","DASH/USDT","NPO/BTC","CRP/USDT","UNI/BTC","BANANA/USDT","DMX/USDT","DFA/USDT","AWT/USDT","CCAR/USDT","XCV/USDT","OM/USDT","MKR/USDT","HAI/USDT","BTRST/USDT","TFC/BTC","LKR/USDT","HEROES/USDT","AST/USDT","AENS/BTC","LRC/ETH","EDHM/USDT","BTC/USDT","XRP/USDT","CONJ/USDT","XEM/ETH","GTN/USDT","JAM/USDT","ADA/USDT","DBC/USDT","BN/USDT","CPAN/USDT","DYDX/USDT","HYDRO/USDT","PIT/USDT","PAXG/USDT","TSX/USDT","REP/BTC","RARE/USDT","CELR/USDT","FOX/USDT","IJC/ETH","TRIBE/USDT","UNO/USDT","LUNA/USDT","PRZ/USDT","POTS/USDT","ASY/USDT","RWN/USDT","ARCX/USDT","LEDU/ETH","EVERETH/USDT","ALICE/USDT","ORBS/USDT","GOL/BTC","SUPER/USDT","OAP/USDT","OCEAN/USDT","PSIX/USDT","WAVES/BTC","TLM/USDT","EOS/ETH","SFC/USDT","SCC/USDT","DG/USDT","BOOMC/USDT","ILV/USDT","SPELL/USDT","DATA/BTC","XRE/USDT","ICE/USDT","HXRO/USDT","AMAS/USDT","FUN/USDT","STR/USDT","AVAX/USDT","ARK/USDT","DCN/USDT","ECTE/BTC","AENS/ETH","FREE/USDT","EOC/USDT","COM/USDT","SLP/USDT","MEAN/USDT","CHESS/USDT","MFTU/USDT","EVY/USDT","ALCX/USDT","ETC/BTC","SI/USDT","ZIL/USDT","EOS/BTC","MAXI/ETH","YOUC/ETH","FXL/USDT","CWAP/USDT","LLG/USDT","VIVID/USDT","MOONSHOT/USDT","INSUR/USDT","PRCH/ETH","FTM/USDT","TOM/USDT","GOL/ETH","SHDC/TRX","NTR/USDT","MPG/ETH","DPR/USDT","SOLX/USDT","CAKE/USDT","AION/ETH","BDA/USDT","ABBC/BTC","COMP/BTC","PURE/USDT","ORK/USDT","VET/USDT","UMA/BTC","PHA/USDT","WEOWNS/USDT","WNXM/USDT","PRCH/TRX","SPH/BTC","CPRO/USDT","BAL/BTC","UFO/USDT","BULL/USDT","GDX/BTC","SYC/ETH","KTN/USDT","D11/USDT","EXRD/USDT","MTRAX/USDT","TVK/USDT","JCC/USDT","XMR/BTC","867/USDT","ERN/USDT","GARI/USDT","BCD/BTC","CHR/USDT","AVINOC/USDT","XTZ/USDT","HERO/USDT","APL/BTC","GLM/ETH","ALPHA/USDT","DBA/USDT","NEO/USDT","HLP/BTC","WAFL/USDT","SKL/USDT","PROMISE/USDT","WACO/BTC","GMT/USDT","UNIS/USDT","SNN/USDT","GAZE/ETH","LMCSWAP/USDT","UNFI/USDT","YGG/USDT","CISLA/USDT","ZEC/BTC","KAU/BTC","HVE2/ETH","WILD/USDT","ANS/USDT","DUSK/USDT","INVESTEL/USDT","TSL/BTC","IOTX/USDT","FANT/USDT","LTC/ETH","BKP/USDT","SPHRI/USDT","BEL/USDT","VPP/USDT","WIVA/USDT","BCH/USDT","SAITAMA/USDT","SHIRYOINU/USDT","CRIC/USDT","FORTH/USDT","BAB/BTC","ZENITH/USDT","RAINBOW/USDT","TIP/USDT","GHC/USDT","CHN/USDT","MATIC/BTC","POWR/BTC","PPT/BTC","LYR/USDT","AVA/USDT","BTRS/USDT","LRC/USDT","FCF/USDT","NUM/USDT","TSA/USDT","JULD/USDT","OIN/USDT","GTC/USDT","DFM/USDT","LINK/BTC","DOGEDASH/USDT","BAND/USDT","SWAT/TRX","REALM/USDT","HOPR/USDT","CRB/USDT","CZB/USDT","DFND/USDT","AQUAGOAT/USDT","NEAR/USDT","INDIA/USDT","QKC/ETH","STSL/USDT","AGLD/USDT","ENTR/USDT","QTUM/ETH","ELON/USDT","CT/USDT","PRCH/USDT","TFC/ETH","NEO/BTC","TABOO/USDT","CBT/USDT","METADOGE/USDT","LUCHOW/USDT","EVY/ETH","CUMSTAR/USDT","FIS/USDT","UCOIN/USDT","ZIL/BTC","STON/BTC","HOT/USDT","BOSON/USDT","BRTR/USDT","ONT/BTC","AGIX/BTC","XPNET/USDT","MMS/USDT","RAT/USDT","YFIH2/USDT","DRSL/USDT","DIGIBET/USDT","ZEC/ETH","THS/USDT","GUM/USDT","WEOWNS/ETH","ARIA20/USDT","OGN/USDT","POWR/ETH","HPNS/USDT","WGL/TRX","DOGO/USDT","DOGE2/USDT","RAY/USDT","GTX/USDT","ANCHOR/USDT","TYPE/ETH","BCMC1/USDT","NXG/USDT","CTC/USDT","NFTB/USDT","FRONT/USDT","EPS/USDT","RNBW/USDT","DOGE/USDT","DINGO/USDT","STARS/USDT","BHF/USDT","ARV/USDT","ULTI/USDT","INDEX/USDT","REN/BTC","ETC/USDT","SHIBELON/USDT","MCAN/USDT","TENSHI/USDT","SUSHI/USDT","MGT/USDT","UNO/BTC","SPH/ETH","SACOI/BTC","SMBSWAP/USDT","DF/USDT","ALPACA/USDT","N1/USDT","DUC/USDT","ZRX/BTC","INFI/USDT","ORBS/ETH","HTK/USDT","AG10/ETH","TKINU/USDT","SONO/USDT","PHR/BTC","SATX/USDT","ELCASH/USDT","FOHO/ETH","TOKAU/USDT","PRCH/LA","ANCHOR/TRX","AUDIO/USDT","TORG/USDT","METAPETS/USDT","CUR/USDT","REEF/USDT","LCX/USDT","BNT/ETH","GFX/USDT","RLC/USDT","FONE/USDT","ETH/USDT","AAVE/ETH","ICX/USDT","OXT/USDT","TUSD/USDT","SAITO/USDT","MOT/USDT","777/USDT","XRP/BTC","QTUM/BTC","DAH/USDT","FIDA/USDT","BSL/ETH","VGL/ETH","MTES/USDT","SRM/USDT","DOT/USDT","REDPANDA/TRX","SNT/ETH","CEEK/ETH","QUACK/USDT","NMR/USDT","SWAPS/USDT","BMT/USDT","PHAE/USDT","CARR/USDT","AGRO/USDT","WTF/USDT","GENE/USDT","LSK/USDT","STON/ETH","CRU/USDT","BLT/USDT","APT/USDT","CMK/USDT","PRO/USDT","DAW/USDT","PXT/USDT","DENT/ETH","NIA/USDT","SBAR/USDT","BIOT/USDT","REP/ETH","RSR/USDT","WACO/ETH","LEASH/USDT","IDLE/USDT","BOBA/USDT","OCTA/USDT","HOHOHO/USDT","ESW/USDT","GEL/USDT","XLM/ETH","SHIB/USDT","ATOM/USDT","PBR/USDT","SAMO/USDT","DEXF/USDT","DNXC/USDT","OOE/USDT","IOWN/USDT","HID/USDT","FALCX/USDT","MPG/BTC","LSS/USDT","FUFU/USDT","OMG/BTC","DPT/USDT","DFI/ETH","LOOKS/USDT","RVN/USDT","SHDC/USDT","KBIT/USDT","GDOG/USDT","MELODY/USDT","FRF/USDT","CELL/USDT","UBXT/USDT","NIJI/USDT","HYBN/ETH","JOYS/USDT","LA/USDT","CAC/USDT","COTI/USDT","DOFI/USDT","GEM/USDT","PRDX/USDT","DGB/BTC","CAS/USDT","SNX/USDT","STORY/USDT","DASH/BTC","BRP/USDT","KSR/USDT","HBAR/USDT","MNST/USDT","JGN/USDT","ELF/BTC","MSD/USDT","LOVELY/USDT","XTM/USDT","LA/ETH","HOKK/USDT","XMAG/USDT","BTS/USDT","CPT/ETH","SPH/USDT","DMLG/USDT","AINU/TRX","FUN/ETH","STORJ/BTC","NPO/USDT","PROMISE/BTC","BTB/USDT","KEEP/USDT","MKR/BTC","SPHN/USDT","MTR/USDT","C98/USDT","AG10/BTC","PHAE/ETH","WAVES/USDT","MNTT/USDT","DXL/USDT","UNI/USDT","ADA/BTC","NU/USDT","ALGO/USDT","UFT/USDT","TRX/BTC","DIVER/USDT","YFI/USDT","WGL/BTC","ENJ/ETH","FESS/USDT","XLM/BTC","NFT/USDT","EGLD/USDT","PALG/USDT","SOV/USDT","DALI/USDT","1SOL/USDT","FIWA/USDT","CRV/USDT","HAPPYDOG/USDT","STARX/USDT","INXT/BTC","BAL/USDT","PAX/USDT","AUCTION/USDT","TLOS/USDT","BKG/USDT","CHAM/BTC","SHIBEMP/USDT","RAMP/USDT","ENJ/BTC","TP3/USDT","LDX/USDT","TCJ/USDT","RANK/USDT","PEOPLE/USDT","SOBA/USDT","UNB/USDT","MPG/USDT","WACO/USDT","GXT/USDT","TOM2/USDT","YOUC/USDT","SFT/USDT","AVINOC/BTC","MRC/TRX","JOB/USDT","TOWER/USDT","AAVE/BTC","CLV/USDT","DYT/USDT","BSL/USDT","AKRO/USDT","FAST/USDT","NECC/USDT","SSB/USDT","SPACE/USDT","UGT/USDT","MFLOKIADA/USDT","DDIM/USDT","JDI/USDT","OVR/USDT","MANA/BTC","CSPR/USDT","FREE/TRX","ATOM/BTC","UMA/USDT","MLN/USDT","AXS/USDT","NFD/USDT","COMP/USDT","PNS/USDT","EVY/LA","BLP/USDT","XLD/USDT","TRYB/USDT","PIG/USDT","BAT/BTC","IMC/USDT","PAINT/USDT","GDT/USDT","ERSDL/USDT","IOWN/ETH","INXT/ETH","LUFFY/USDT","BMT/TRX","EOS/USDT","BADGER/USDT","QBU/USDT","BOTX/USDT","BTT/TRX","OCB/USDT","ATOLO/BTC","FUFI/USDT","XED/USDT","XTZ/BTC","JCH/USDT","STMX/USDT","GALA/USDT","AFIN/ETH","R1/USDT","LTC/BTC","GRT/USDT","METIS/USDT","PLOCK/USDT","RBN/USDT","BCOIN/USDT","TRX/ETH","ONT/ETH","CBA/USDT","EVA/USDT","MBOX/USDT","SUSHI/BTC","2LC/USDT","KNC/USDT","CVX/USDT","SWM/USDT","PTA/USDT","WENLAMBO/USDT","QIN/USDT","HPE/USDT","XFIT/USDT","SACOI/USDT","REN/USDT","BN/ETH","MSOT/BTC","MFLATE/USDT","BETA/USDT","BA/USDT","DOLPH/USDT","NEVADA/USDT","BIT/USDT","NABOX/USDT","RACA/USDT","WSPP/USDT","EURU/USDT","AKITA/USDT","BAT/ETH","NIT/ETH","BABYDOGE/USDT","WHX/USDT","WAR/USDT","GNO/USDT","MNTG/USDT","UMAD/USDT","TERC/USDT","POLS/USDT","KISHU/TRX","RYIP/USDT","GOL/USDT","ESTI/BTC","RWN/BTC","BIFI/USDT","OAP/ETH","DYN/USDT","SHIBA/USDT","DFI/BTC","AIRX/ETH","BTCBANK/USDT","LINK/USDT","ORBS/BTC","SIF/USDT","DPET/USDT","GHD/ETH","DATA/USDT","FSHN/USDT","DODO/USDT","LINA/USDT","CFXQ/USDT","TBT/USDT","STARL/USDT","GOLDUCK/USDT","XRP/ETH","WIN/USDT","SUN/BTC","AENS/USDT","PERP/USDT","BURGER/USDT","JASMY/USDT","ONT/USDT","SNT/BTC","ACH/USDT","CLS/USDT","MTR/TRX","SPH/TRX","CNF/USDT","WDR/USDT","FOHO/BTC","TANGO/USDT","ATA/USDT","PRCH/BTC","WHXCV/USDT","INJ/USDT","CRIC/BTC","SMBSWAP/ETH","YFIH2/BTC","WHXC/USDT","IOST/USDT","YIELD/USDT","IDEX/USDT","JOYS/BTC","S4F/ETH","FLX/USDT","CNT/USDT","BEER/TRX","IOTA/USDT","META/USDT","BLOVELY/USDT","DEXE/USDT","NEXO/USDT","ZEC/USDT","NAME/USDT","NITRO/USDT","ZIL/ETH","IJC/USDT","LOOM/ETH","CYFM/USDT","GHST/USDT","MATIC/USDT","QRT/USDT","BUX/USDT","TRDC/USDT","ILUS/USDT","PQT/USDT","DIXT/USDT","CT/BTC","SPCPPR/USDT","BCH/BTC","AIRX/USDT","MAP/USDT","WTC/BTC","WNXM/BTC","FOHO/USDT","DNT/USDT","LSK/ETH","LOOM/BTC","7HR/USDT","XMR/USDT","FREN/USDT","KEX/USDT","AGAIN/ETH","OMG/USDT","S4F/BTC","SPRT/USDT","MANA/ETH","DBX/USDT","DAH/ETH","YFII/USDT","MVC/USDT","LACE/USDT","STOS/USDT","XVS/USDT","ACTI/USDT","MASK/USDT","TKG/USDT","SDBY/TRX","PROM/USDT","LPT/USDT","DGB/USDT","JOYS/ETH","LMCSWAP/BTC","DSFR/USDT","LSK/BTC","ZKS/USDT","DFI/USDT","FET/USDT","HYBN/USDT","USDC/USDT","ICX/ETH","SHON/USDT","AVINOC/ETH","LINK/ETH","CVT/USDT","VET/ETH","CTSI/USDT","USDU/USDT","PTF/USDT","QRDO/USDT","HOD/USDT","WOD/USDT","REVV/USDT","ROYA/USDT","CELO/USDT","RBIS/USDT","DLEGENDS/USDT","LMCSWAP/ETH","KLV/USDT","LOL/ETH","AGX/USDT","OKS/USDT","HVE2/USDT","TPOS/USDT","DFC/USDT","RLC/BTC","ICX/BTC","ETERNAL/USDT","PROPEL/USDT","BLI/USDT","SRM/BTC","AZUM/USDT","BTT/USDT","XRE/TRX","DAH/BTC","KAI/USDT","KABOSU/USDT","PORTO/USDT","BAND/BTC","PKF/USDT","CVC/USDT","LA/BTC","HCS/USDT","PHAE/BTC","ANT/USDT","PPAY/USDT","RAT/ETH","HOTCROSS/USDT","SOL/USDT","MARSINU/USDT","JSB/USDT","LRC/BTC","HAM/USDT","LTC/USDT","FARM/USDT","HSBT/USDT","KLC/USDT","HOT/ETH","DOGS/USDT","DGCL/USDT","EQZ/USDT","FF/USDT","DOTX/USDT","XLM/USDT","ALGO/BTC","RAD/USDT","HIDEOUS/USDT","GDM/USDT","COMBO/USDT","VLX/USDT","JCO/USDT","BTCV/BTC","LQTY/USDT","STON/USDT","EDN/USDT","API3/USDT","POLY/BTC","DMD/USDT","ETH/BTC","RFX/USDT","ZRX/USDT","REVA/USDT","STRIP/USDT","QTUM/USDT","FLOKI/USDT","DOT/BTC","RTF/USDT","GLC/USDT","BCMC1/ETH","BAKE/USDT","GLV8/USDT","GMY/USDT","AGOLP/USDT","KINGSHIB/USDT","BTG/BTC","BMH/BTC","ICP/USDT","TYPE/USDT","BOZKURT/USDT","BRMT/USDT","LBXC/USDT","ORN/USDT","TTT/USDT","UCOIN/BTC","CLION/USDT","LIT/USDT","ARPA/USDT","XYM/USDT","DCR/BTC","RWN/ETH","1INCH/USDT","YOUC/BTC","SNB/USDT","KAIECO/USDT","CER/USDT","CTT/USDT","WSG/USDT","BLOK/USDT","HMT/USDT"]
app = Flask(__name__)
while True:
    index = -1
    json_response_new = get_token()
    #print("json_response_new",json_response_new)
    json_response_new_len = len(json_response_new)
    list_o_new = []
    list_o_new_notricker = []
    s = ","
    s1 = ","
    
    

    for j in json_response_new:
        baseCurrency = j['baseCurrency']
        quoteCurrency = j['quoteCurrency']
        list_o_new_notricker.append(j['symbol'])
        if j['lastPrice']!="0":
            list_o_new.append(j['symbol'])
    difference_1 = list(set(list_o_new).difference(set(list_all_token)))
    difference_2 = list(set(list_o_new_notricker).difference(set(list_all_token)))
    s = s.join(difference_1)+"new token is: "+str(len(difference_1))
    s1 = s1.join(difference_2)+"new token is: "+str(len(difference_2))
    
    
    
    if len(difference_1)>=1:
        for j in json_response_new:
            baseCurrency = j['baseCurrency']
            quoteCurrency = j['quoteCurrency']
            a_price = float(j['lastPrice'])
            if j['lastPrice']!="0":
                if(j['symbol']=="TULIP"+"/USDT") and j['symbol'] in difference_1:
                    #place_order(baseCurrency,quoteCurrency,1.12345699,9) # 10 $
                    place_order(baseCurrency,quoteCurrency,2.1283699,9.3968) # 20 $
                    place_order(baseCurrency,quoteCurrency,3.273728,4.58) # 15$
                    place_order(baseCurrency,quoteCurrency,5,2) # 10$
                    place_order(baseCurrency,quoteCurrency,10,0.5) # 5 $
                if(j['symbol']=="RYLT"+"/USDT") and j['symbol'] in difference_1:
                    place_order(baseCurrency,quoteCurrency,0.0456798,220) # 10$
                    place_order(baseCurrency,quoteCurrency,0.0123456,805) # 10$
                    place_order(baseCurrency,quoteCurrency,0.0055678,2694) # 15$
                    place_order(baseCurrency,quoteCurrency,0.0022848,6565) # 15 $
                    place_order(baseCurrency,quoteCurrency,0.0005168,29024) # 15$
                if(j['symbol']=="QTCT"+"/USDT") and j['symbol'] in difference_1:
                    place_order(baseCurrency,quoteCurrency,1.12345699,9) # 10$
                    place_order(baseCurrency,quoteCurrency,2.1283699,9.3968) # 20$
                    place_order(baseCurrency,quoteCurrency,3.273728,4.58) # 15$
                    place_order(baseCurrency,quoteCurrency,5,2) # 10$
                    place_order(baseCurrency,quoteCurrency,10,0.5) # 5$
                if(j['symbol']=="KAIDHT"+"/USDT") and j['symbol'] in difference_1:
                    place_order(baseCurrency,quoteCurrency,5,1) # 5$
                    place_order(baseCurrency,quoteCurrency,2.12335454,5) # 10$
                    place_order(baseCurrency,quoteCurrency,1,20) # 20$
                    place_order(baseCurrency,quoteCurrency,0.6,25) # 15$
                if(j['symbol']=="SHREE"+"/USDT") and j['symbol'] in difference_1:
                    place_order(baseCurrency,quoteCurrency,0.000012345,810044) # 10$
                    place_order(baseCurrency,quoteCurrency,0.000003349,5971931) # 20$
                    place_order(baseCurrency,quoteCurrency,0.000001345,14869888)# 20$ 
        message = client.api.account.messages.create(  
                              messaging_service_sid='MG78d527f0a5e19ef93a15178c3942f41d', 
                              body=s,      
                              to='+919785466389' 
                          )
        # print(message)
        #print("ticker",s,len(difference_1),len(json_response_new))
        list_all_token.extend(difference_1)
    else:
        print("len is 0")
    if len(difference_2)>=1:
        message = client.api.account.messages.create(  
                              messaging_service_sid='MG78d527f0a5e19ef93a15178c3942f41d', 
                              body=s,      
                              to='+919785466389' 
                          )
        print(message)
        print("all token",s1,len(difference_2),len(json_response_new))
    else:
        print("len is 0")
    time.sleep(60)


