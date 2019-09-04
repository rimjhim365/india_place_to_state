import time
import sys
locationD={'andhra pradesh':['adoni','chilakaluripet','kadiyam','tadepalligudem','tadipatri','narasaraopet','gudivada','dharmavaram','tenali','srikakulam','madanapalli','guntakal','madanapalle','bhimavaram','hindupur','proddatur','andhra pradesh','Visakhapatnam','Vizag','Vijayawada','hyderabad','rajahmundry','vizianagaram','machilipatnan','nandyal','eluru','ongole','guntur','warangal','vijaywada','tirupati','andhra','ananthapur','Nellore','Kurnool','Kadapa','East Godavari','Vizianagaram','Prakasam','Kurnool','Kurnool','Guntur','Kadapa','Chittoor','Srikakulam','anantpur','Krishna','Anantapur','West Godavari','kakinada','warangal','Nizamabad','karimnagar','khammam','nalgonda','ramagundam','mahbubnagar','mancherial','adilabad','kamareddy','bhupalpalle','nagarkurmool','kothagudem','asifabad','sangareddy','vikarabad','telangana','kottagudem'],

'Arunachal Pradesh':['arunachal','Arunachal Pradesh','Itanagar','Tawang','Bhismaknagar','Malinithan','arunchal','Ziro','Bomdila','Pasighat','Bhalukpong','naharlagun'],

'Assam':['sonitpur','kamrup','cachar','guwahati','silchar','tezpur','dibrugadh','tinsukhiya','assam','jorhat','nagaon','karimganj'],
'Bihar':['bihar','nalanda','patna','gaya','bhagalpur','muzaffarpur','katihar','purnea','buxar','bettiah','Darbhanga','Bihar Sharif','Arrah','Begusarai','Katihar','Munger','Chhapra','Danapur','Saharsa','Sasaram','Hajipur','Dehri','Siwan','Motihari','Nawada','Bagaha','Buxar','Kishanganj','Sitamarhi','Jamalpur','Jehanabad','Aurangabad'],
'Chhattisgarh':['Chhattisgarh','raipur','corba','durg bhilai','bhilai','chhattisgadh','chatisgadh','chattisgadh','chhatisgadh','Durg','Bhilai','Korba','Rajnandgaon','Raigarh','Jagdalpur','Ambikapur','Chirmiri','Raipur','Dhamtari','Mahasamund'],
'Goa':['panaji','margao','goa','Mormugao','Madgaon','vascodagama','vasco da gama','mapusa','ponda','old goa','calangute','canacona'],
'Gujarat':['dabhoi','hazira','siddhpur','modhera','dharampur','modasa','amreli','wankaner','kandala','himatnagar','visnagar','vadnagar','champaner','khanbhat','navagadh','chhota udaipur','chota udaipur','valsad','mandvi','godhra','botad','saputara','palitana','gondal','ahmedabad','suraj','vadodara','rajkot','bhuj','dwarka','gujarat','gujrat','Surat','Vadodara','Bhavnagar','Jamnagar','Junagadh','Gandhidham','Nadiad','Gandhinagar','Anand','Morbi','Surendranagar','Bharuch','Vapi','Navsari','Veraval','Porbandar','Godhra','Bhuj','Ankleshwar','Botad','Palanpur','Patan','Dahod','Jetpur','Valsad','Kalol','Gonda','Amreli','Mehsana'],
'Haryana':['fatehabad','kurushetra','kurukshetra','narnaul','mahendragarh','gurugram','gurgaon','faridabad','panipath','ambala','haryana','Faridabad','Gurgaon','Panipat','Ambala','Yamunanagar','Rohtak','Hisar','Karnal','Sonipat','Panchkula','Bhiwani','Sirsa','Bahadurgarh','Jind','Thanesar','Kaithal','Rewari','Palwal'],
'Himachal Pradesh':['narkanda','naina devi','nainadevi','bakloh','rewalsar','jutogh','dagshai','sabathu','theog','nadaun','jhakhri','sarkaghat','jogindernagar','dera gopipur','jawalamukhi','nagrota bagwan','rohru','ghumarwin','parwanoo','shamshi','basdehra','mehatpur','santokhgarh','kangra','nurpur','Himachal Pradesh','shimla','Kufri','Kullu Manali','Rohtang Pass','Dharamshala','Dalhousie','Khajjiar','Chail','Kasauli','Lahaul' 'Spiti','Solan','Palampur','Chamba','Kangra Valley','Hamirpur','himachal','paonta sahib','Kinnaur','Mandi','Nahan','Nalagarh','Parwanoo','Pathankot','Pragpur','Una','Manali','Kullu','Spiti',],
'Jammu and Kashmir':['jasrota','manhasan','gho','samba','matho','achaban','badami bagh','qazigund','beerwah','patnitop','handwara','pulwama','kokernag','kupwara','magam','charari','shangus','poonch','khan sahib','khan saheb','bhadrawah','uri','verinag','basholi','shupiyan','rajouri','pattan','kishtwar','kathua','akhnoor','kargil','Jammu and Kashmir','srinagar','jammu','anantnag','kashmir','Jammu','Srinagar','Leh','Ladakh','Gulmarg','Sonamarg','Pahalgam','Udhampur','kathua','bandipura','baramula','sopore'],
'Jharkhand':['bandhgora','ghorabandha','jaridih','gomoh','chhota gobindpur','chota gobindpur','netarhat','garhwa','jharia','sirka','pakur','topchanchi','malkera','kanke','barkakana','madhupur','chandrapura','bundu','rajmahal','gomia','jugsalai','bermo','ghatshila','gumla','maithom','patratu','jhumri telaiya','dumka','chirkunda','phusro','adityapur','chas','chaibasa','daltongang','ranchi','bokaro','jamshedpur','jharkhand','palamu','ramgadh','giridih','hazaribag','deoghar','phusro','chirkunda','medininagar'],
'Karnataka':['bangalore','dandeli','llkal','aiholi','bagalkot','doddaballapura','sringeri','halebidu','hubali','robertsonpet','channapatna','pattadakal','kolar','madikeri','chikmagalur','koppal','belur','srirangapatna','ranebennuru','hampi','bengaluru','manglore','dharwad','mangalore','hasan','mysore','hubli','badami','gulbarga','karnataka','mangalore','mangaluru','Hubli','Dharwar','Belgaum','Davanagere','Bellary','hospet','shimoga','betageri','gadag','Bijapur','Shimoga','Tumkur','Raichur','udupi','Bidar','Hospet','Hassan','Gadag Betigeri','Udupi','Robertson','Bhadravati','Chitradurga','Kolar','Mandya','Chikmagalur','Gangawati','Bagalkot','shimoga'],
'Kerala':['kuttanad','kalpetta','beypore','manjeri','paravur','angamaly','koyilandy','neyyattinkara','shoranur','payyanur','malampuzha','vatakara','taliparamba','attingal','calicut','ottapalam','pathananthitta','ernakulam','thiruvalla','ponnani','kumarakom','punalur','tirur','thalassery','guruvayur','kovalam','varkala','kannur','alappuzha','thrissur','kasaragod','trivandrum','kochi','kozhikode','kollam','palakkad','munnar','kerala','keral','Kayamkulam','Malappuram','Thiruvananthapuram','Kottayam','Cherthala'],
'Madhya Pradesh':['Madhya Pradesh','maihar','chhatarpur','vidisha','amarkantak','chanderi','maheshwar','guna','bhedaghat','panna','orchha','mandsaur','pachmadhi','pachmarhi','chhindwara','khajuraho','madya pradesh','Indore','ujjain','jabalpur','gwalior','sanchi','morena','dhar','narsinghgarh','pithampur','khargone','rewa','bhopal','gwalior','madhya','Sagar','Dewas','etawa','mhow','mandideep','satna','Ratlam','Rewa','Murwara','Katni','Singrauli','Burhanpur','chitrakut','chitrakoot','Khandwa','Bhind','Chhindwara','Guna','Shivpuri','Vidisha','Chhatarpur','Damoh','Mandsaur','Khargone','Neemuch','Pithampur','Hoshangabad','Itarsi','Sehore','Betul','Seoni','Datia','Nagda'],
'Maharashtra':['pandharpur','ellora','virar','vasai','vasai-virar','washim','buldhana','hingoli','mahabaleshwar','ahmednagar','bhusaval','beed','karad','ambarnath','nagar','ulhasnagar','khandala','chikaldara','ichalkarangi','baramati','panchagani','chiplun','nasik','matheran','satara','panvel','shirdi','lonavla','lonavala','dombivli','kalyan','pune','nagpur','nashik','thane','Pimpri','Chinchwad','alibag','amravati','amrawati','mumbai','maharashtra','bombay','Vasai','Virar','Solapur','Bhiwandi','Amravati','Malegaon','Kolhapur','Nanded','Sangli','Sangali','Jalgaon','Akola','Latur','Ahmadnagar','Dhule','Ichalkaranji','Chandrapur','Parbhani','Jalna','Bhusawal','Navi Mumbai','Panvel','solapur','bhiwandi'],
'Manipur':['pakhanglakpa','sugnu','naoriya','lamgaotongba','sekmai','sikhong','thongkong','nungba','porompat','samurou','shirui','lamshang','khunou','lilong','wangoi','kumbi','noney','heriok','oinam','kamjong','kwakta','lamai','andro','bishnupur','moreh','jiribam','wangjing','ukhrul','kangpokpi','yairipuk','tamenglong','thoubal','nambol','ningthoukhong','moirang','manipur','imphal','kakching','Mayang Imphal','Thoubal','Ukhrul'],
'Meghalaya':['mawlai','mankachar','pynthorumkhrah','balat','dispur','madanrting','cherrapunji','tura','nongpoh','baghmara','garo','mirang','resubelpara','nongthymmai','meghalaya','shillong','Williamnagar','jowai','Nongstoin'],
'Mizoram':['lunglei','mizoram','aizwal','Lawngtlai','kolasib','Champhai'],
'Nagaland':['ngwalwa','nsong','khelma','punglwa','poilwa','jalukie','tizit','tening','ahthibung','viswema','benreu','jotsoma','longleng','kiphire','tuli','phek','changtongya','khonoma','peren','chumukedima','mon','mokokchung','zunheboto','tuensang','wokha','nagaland','Mokokchung','kohima','Chumukedima'],
'Orissa':['bhubneshwar','hirakund','hirakud','rajgangpur','burla','boudh','pipli','gopalpur','paradip','bhawanipatna','kalhandi','bhubaneshwar','orissa','odisha','odisa','berhampur','konark','dhenkalanal','baripada','barbil','Khurda','Cuttack','Rourkela','Brahmapur','talcher','angul','phulbani','chandipur','gunupur','jatani','jhasuguda','sunabeda','jaleswar','Sambalpur','Puri','Balasore','Bhadrak','Baripada','Jharsuguda','Jeypore','baleshwar'],
'Punjab':['sri muktsar','khanna','abohar','amritsar','ludhiyana','jalandhar','mohali','patiala','punjab','chandigarh','chandigadh','Bathinda','Hoshiarpur','Gurdaspur','Pathankot','Moga','Fazilka','Muktsar','Barnala','Firozpur','Kapurthala','Sangrur','batala'],
'Rajasthan':['jhalawar','bhilwara','nohar','nagaur','lakshamangarh','laxmangarh','phalodi','bhiwadi','Jodhpur','udaipur','kota','pushkar','jaisalmer','bikaner','ajmer','rajasthan','Alwar','mandawa','Bharatpur','Sikar','Pali','Chittorgarh','Tonk','Kishangarh','Beawar','Hanumangarh','Dholpur','Gangapur','Hindaun City','Sawai','Madhopur','Churu','jaipur','amer','bundi','ranakpur','nawalgarh'],
'Sikkim':['pelling','yuksom','gyalshing','singtam','chungthang','richenpong','soreng','legship','gangtok','sikkim','Geyzing','mangan','namchi','jorethang','rangpo'],
'Tamil Nadu':['kanyakumari','pudukkottai','kuddalore','kodaikanal','rameshwaram','rameswaram','trichy','trichi','Tamil Nadu','madurai','coimbatore','tiruchirapalli','vellore','ooty','Tamil','Chennai','Tiruppur','Salem','Erode','Tirunelveli','Thoothukkudi','Nagercoil','Thanjavur','Dindigul','Cuddalore','Kanchipuram','Tiruvannamalai','Kumbakonam','Rajapalayam','Pudukottai','Hosur','Ambur','Karaikkudi','Neyveli','Nagapattinam'],
'Tripura':['dharmanagar','sabroom','khowai','ambassa','sonamura','kamalpur','ranirbazar','kumarghat','melaghar','badharghat','gakulnagar','charipara','indranagar','joynagar','tripura','agartala','belonia','bishalgarh','kailashahar','udaipur','teliamura'],
'Uttaranchal':['vikasnagar','laksar','sitarganj','bhowali','khatima','kathgodam','kedarnath','tehri','haldwani','dehradun','roorkee','haridwar','rishikesh','mussoorie','nainital','badrinath','Uttaranchal','uttranchal','uttarakhand','haridwar','ramnagar','manglaur','pithoragarh','kashipur','rudrapur'],
'Uttar Pradesh':['naihati','suri','shravasti','kaushambi','bagpat','ayodhya','behraich','kashi','Uttar Pradesh','kanpur','banaras','allahabad','agra','noida','mathura','Lucknow','Ghaziabad','Varanasi','Meerut','Bareilly','Aligarh','Moradabad','Saharanpur','Gorakhpur','Faizabad','Jhansi','Muzaffarnagar','Mathura','Budaun','Rampur','Shahjahanpur','Farrukhabad','Hapur','Noida','Etawah','Mirzapur','Bulandshahr','Sambhal','Amroha','Hardoi','Fatehpur','Raebareli','Orai','Sitapur','Bahraich','Modinagar','Unnao','Jaunpur','Lakhimpur','Hathras','Banda','Pilibhit','Mughalsarai','Barabanki','Khurja','Gonda','Mainpuri','Lalitpur','Etah','Deoria','Ujhani','Ghazipur','Sultanpur','Azamgarh','Bijnor','Sahaswan','Basti','Chandausi','Akbarpur','Ballia','Tanda','Greater Noida','Shikohabad','Shamli','Khair','Kasganj'],
'West Bengal':['dumdum','baruipur','chandannagar','belurghat','kalyani','barrackpore','kalimpong','bidhan nagar','West Bengal','durgapur','asansol','darjeeling','howrah','kolkata','calcutta','kharaghpur','Siliguri','Bardhaman','Baharampur','Habra','Kharagpur','Shantipur','Dankuni','Dhulian','Ranaghat','Haldia','Raiganj','Krishnanagar','Nabadwip','Midnapore','Jalpaiguri','Balurghat','Basirhat','Bankura','Chakdaha','Alipurduar','Purulia','Jangipur','Bangaon','cooch','Cooch Behar','bengal','bangal'],
'Andaman and Nicobar Islands':['Andaman and Nicobar Islands','andman','andmaan','Prothrapur','Garacherama','garacherama','portblair','bamboo flat','nicobar','blair'],
'DadarNagar':['dadar','nagar haveli','Samarvarni','dadra'],
'Daman and Diu':['daman','diu','Kachigam'],
'Delhi':['delhi','new delhi','dilli','NCR','Qutabgarh','Jaffarpur Kalan'],
'Lakshadweep':['lakshadeep','lakshadweep','lakshdweep','lakshdeep','Kavaratti','andrott','minicoy'],
'Pondicherry':['puduchery','pondicherry','yanam','karikal','puducherry','mahe']
     }
zoneD={'northern':['Delhi','Haryana','Himachal Pradesh', 'Jammu and Kashmir', 'Punjab','Rajasthan'],'central':['Chhattisgarh','Madhya Pradesh','Uttaranchal','Uttar Pradesh'],'eastern':['Bihar','Jharkhand','Orissa','West Bengal'],'western':['DadarNagar','Daman and Diu','Goa','Gujarat','Maharashtra'],'southern':['andhra pradesh', 'Karnataka','Kerala','Lakshadweep','Pondicherry','Tamil Nadu','Telangana'],'northeastern':['Assam','Arunachal Pradesh','Manipur','Meghalaya','Mizoram','Nagaland','Tripura','sikkim']}
