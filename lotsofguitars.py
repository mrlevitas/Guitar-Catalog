from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import guitarType, Base, guitarInfo, User

# engine = create_engine('sqlite:///guitarCatalog.db')

engine = create_engine('sqlite:///guitarCatalogwithusers.db')

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTs3mRtcsyl7kj5OjKwX_9lnBD3JCeeQldDxPeWMq3Q8TvLkUe0Rg')
session.add(User1)
session.commit()


# Entry for acoustic guitar
guitar1 = guitarType(user_id=1, name="Acoustic Guitar")
session.add(guitar1)
session.commit()

# Entry for electric guitar
guitar2 = guitarType(user_id=1, name="Electric Guitar")
session.add(guitar2)
session.commit()

# Entry for left-handed guitar
guitar3 = guitarType(user_id=1, name="Left-handed Guitar")
session.add(guitar3)
session.commit()

# Entry for ukulele
guitar4 = guitarType(user_id=1, name="Ukulele")
session.add(guitar4)
session.commit()


# Entry for acoustic bass guitar
guitar5 = guitarType(user_id=1, name="Acoustic Bass")
session.add(guitar5)
session.commit()

# Entry for electric bass guitar
guitar6 = guitarType(user_id=1, name="Electric Bass")
session.add(guitar6)
session.commit()

# Entry for upright bass guitar
guitar7 = guitarType(user_id=1, name="Upright Bass")
session.add(guitar7)
session.commit()





# populate acoustic guitars into database
# typeOfGuitar = guitar1 

# http://www.guitarcenter.com/Gibson-Hummingbird-Pro-Cutaway-Acoustic-Electric-Guitar-105494314-i1476553.gc
acoustic1 = guitarInfo(user_id=1, name="Gibson Hummingbird Pro Cutaway Acoustic-Electric Guitar", description="A true legend of acoustic instruments, the Gibson Hummingbird Pro acoustic-electric guitar was first introduced in 1960 as Gibson's earliest square-shoulder dreadnought. Superb for all styles of playing, with a capacity for rich, first-position folk chords and intricate solo playing, the Hummingbird quickly became the icon of the Gibson acoustic line, and a favorite among legends like Gram Parsons and Keith Richards. The Hummingbird acoustic-electric guitar has been one of Gibson Acoustic's most enduring guitars.",
                     price="$2,199.00", stringNum="6", typeOfGuitar =guitar1)

session.add(acoustic1)
session.commit()


# http://www.guitarcenter.com/Martin-15-Series-00015M-Acoustic-Guitar-105921852-i1512934.gc
acoustic2 = guitarInfo(user_id=1, name="Martin 15 Series 00015M Acoustic Guitar", description="The Martin 00015M offers a perfect blend of vintage features and modern technology to create an acoustic guitar of exceptional tone, playability and classic Martin good looks. Back, sides and top are bookmatched solid genuine mahogany with A-frame Sitka Spruce X-bracing and a traditional maple bridge-plate. The 14-fret neck-also genuine mahogany-is joined with an East Indian rosewood fingerboard and headplate. The traditional rosewood belly-bridge is fitted with a bone saddle, and the nut is fashioned from bone as well. ",
                     price="$1,249.00", stringNum="6", typeOfGuitar =guitar1)

session.add(acoustic2)
session.commit()


# http://www.guitarcenter.com/Yamaha-F335-Acoustic-Guitar-102919487-i1166364.gc
acoustic3 = guitarInfo(user_id=1, name="Yamaha F335 Acoustic Guitar", description="Yamaha's F335 gives you that classic dreadnought shape and sound at a price point that won't break your bank. The F335's tonewood combination includes a laminate spruce top, rosewood fingerboard and bridge, and meranti back and sides. Gold die-cast tuners provide smooth and accurate tuning while a tortoiseshell pickguard gives a bit more style. Case sold separately.",
                     price="$159.99", stringNum="6", typeOfGuitar =guitar1)

session.add(acoustic3)
session.commit()

# http://www.guitarcenter.com/Ibanez-V70CE-Acoustic-Electric-Guitar-102567492-i1150613.gc
acoustic4 = guitarInfo(user_id=1, name="Ibanez V70CE Acoustic-Electric Guitar", description="Acoustic electric guitar with select spruce top and mahogany back and sides. Mahogany neck. The V70CE is equipped with a soft cutaway for higher access. It is a very responsive instrument with capacity for great dynamic range both acoustically and through the output.",
                     price="$174.00", stringNum="6", typeOfGuitar =guitar1)

session.add(acoustic4)
session.commit()

# http://www.guitarcenter.com/Fender-CD-60-Dreadnought-Acoustic-Guitar-108408956-i1709795.gc 
acoustic5 = guitarInfo(user_id=1, name="Fender CD-60 Dreadnought Acoustic Guitar", description="Want features you'd expect in a much more expensive instrument? The CD-60 is your guitar, with features including a spruce top, mahogany back and sides, die-cast tuners, and an included hardshell case.",
                     price="$229.99", stringNum="6", typeOfGuitar =guitar1)

session.add(acoustic5)
session.commit()

# http://www.guitarcenter.com/Ovation-Standard-Balladeer-2751-AX-12-String-Acoustic-Electric-Guitar-620757-i1470173.gc
acoustic6 = guitarInfo(user_id=1, name="Ovation Standard Balladeer 2751 AX 12-String Acoustic-Electric Guitar Black", description="The 12-string Ovation Standard Balladeer 2751 AX is a gorgeous acoustic-electric guitar with a super shallow cutaway body and an AA solid spruce top. The 12-string guitar has scalloped X-bracing, a rosewood fretboard and bridge, chrome tuning machines, and an inlaid pearl oak leaf rosette. The onboard Ovation OCP-1K pickup delivers classic Ovation guitar tone for a great plugged-in experience.",
                     price="$799.00", stringNum="12", typeOfGuitar =guitar1)

session.add(acoustic6)
session.commit()

#http://www.guitarcenter.com/Taylor-K66-Koa-Grand-Symphony-12-String-Acoustic-Guitar-109157743-i3125295.gc
acoustic7 = guitarInfo(user_id=1, name="Taylor K66 Koa Grand Symphony 12-String Acoustic Guitar Shaded Edgeburst", description="The K66-SEB GS 12-String Acoustic Guitar features Hawaiian koa top, back and sides, a wood with captivating beauty that is matched by a tone that blossoms over time, especially in the midrange. Its voice is bright and focused, with warm overtones that slowly emerge, adding sweetness and depth. Premium all-wood appointments, led by the Island Vine fingerboard inlay, celebrate the wood's natural appeal on this Grand Symphony shaped body.",
                     price="$3,799.00", stringNum="12", typeOfGuitar =guitar1)

session.add(acoustic7)
session.commit()


# http://www.guitarcenter.com/Ibanez-AEL207E-7-String-Acoustic-Electric-Guitar-109319269-i3219358.gc
acoustic8 = guitarInfo(user_id=1, name="Ibanez AEL207E 7-String Acoustic-Electric Guitar Trans Black Sunburst", description="The Ibanez AEL207E 7-String Acoustic-Electric Guitar with Onboard Tuner is as sweet to your ears as it is beautiful to your eyes. A Fishman Sonicore pickup and SST preamp deliver outstanding reproduction of the guitar's acoustic tone. The AEL207E features a flamed maple top with maple back and sides for a tight, well-balanced sound across all 7 strings. It comes with a rosewood fretboard and bridge, die-cast gold tuners, pearl dot inlays and an onboard tuner.",
                     price="$499.99", stringNum="7", typeOfGuitar =guitar1)

session.add(acoustic8)
session.commit()
















# populate electric guitars into database
# typeOfGuitar = guitar2

# http://www.guitarcenter.com/Fender-American-Deluxe-Telecaster-Ash-Electric-Guitar-105936371-i1519106.gc
electric1 = guitarInfo(user_id=1, name="Fender American Deluxe Telecaster Ash Electric Guitar Butterscotch Blonde", description="Tone, tradition and innovation. Fender's new American Deluxe Telecaster is the 21st century way to rock with a Telecaster, graced by the added distinction of a traditional ash body. The compound radius fretboard allows effortless string bending anywhere along the neck, and staggered locking tuners improve tuning stability for stunt guitarists who like to bend behind the nut. New N3 Noiseless pickups provide improved Telecaster tones for snappy bell-like chime with no the hum; other features include S-1 switching and chromed brass bridge saddles.",
                     price="$1,749.99", stringNum="6", typeOfGuitar =guitar2)

session.add(electric1)
session.commit()

# http://www.guitarcenter.com/ESP-LTD-Deluxe-EC-1000-Electric-Guitar-105316434-i1149000.gc
electric2 = guitarInfo(user_id=1, name="ESP LTD Deluxe EC-1000 Electric Guitar", description="Pick up the ESP LTD Deluxe EC-1000 Electric Guitar and you'll believe this lightweight beauty can do it all. It's purposefully built for maximum crunch with its mahogany body, set mahogany-scale neck, and rosewood fretboard (ebony on vintage black). Abalone flags plus the model name at the 12th fret give it distinction. The TonePros locking bridge and tailpiece keep tuning rock-solid. It features a flamed maple top and a pair of active EMG-81/60 pickups, except the amber sunburst model that sports a Seymour Duncan JB/59 passive pickup setup.",
                     price="$849.00", stringNum="6", typeOfGuitar =guitar2)

session.add(electric2)
session.commit()


# http://www.guitarcenter.com/Schecter-Guitar-Research-Hellraiser-C-1-Electric-Guitar-103135695-i1446249.gc
electric3 = guitarInfo(user_id=1, name="Schecter Guitar Research Hellraiser C-1 Electric Guitar", description="The Schecter Hellraiser C-1 is an electric guitar that delivers tones guaranteed to satisfy any metal player. The Hellraiser's mahogany body has an ultra-access cutaway that really lets you get all the way up the 3-piece mahogany neck. The rosewood fretboard on the Hellraiser C-1 has 24 extra-jumbo frets and gothic cross inlays for an edgy look. Active EMG 81TW and 89 humbuckers deliver crushing electric guitar tone. Now you have more options that ever by activating single-coil sounds via push/pull volume knobs.",
                     price="$799.00", stringNum="6", typeOfGuitar =guitar2)

session.add(electric3)
session.commit()

# http://www.guitarcenter.com/Ibanez-JS1200-Joe-Satriani-Signature-Guitar-103522397-i1150595.gc
electric4 = guitarInfo(user_id=1, name="Ibanez JS1200 Joe Satriani Signature Guitar Candy Apple", description="If fast solos and sweet tone are your thing, you'll love the Ibanez JS1200 Joe Satriani Signature Guitar. It took Ibanez many years to create guitars that would satisfy the Master of Tone, and the result is superb! Precision-sculpted basswood body is light on the shoulder with otherworldly looks and great high-fret access. Its vibrant resonance is translated into endless sustain through DiMarzio humbuckers -- a PAF Joe at the neck and a Fred at the bridge. Screamin' fast JS Prestige maple neck features smaller 6105 frets and tighter radius on a rosewood fretboard. Dive bomb with aplomb on the Edge bridge.",
                     price="$2,199.99", stringNum="6", typeOfGuitar =guitar2)

session.add(electric4)
session.commit()

# http://www.guitarcenter.com/ESP-LTD-EC-1000T-CTM-Traditional-Custom-Electric-Guitar-106732340-i1797724.gc
electric5 = guitarInfo(user_id=1, name="ESP LTD EC-1000T/CTM Traditional Custom Electric Guitar Snow White", description="The LTD Deluxe EC-1000T/CTM has that custom look that you've probably cherished. It's a classic single-cutaway mahogany guitar with a traditional body shape dressed up with top and back binding. The set mahogany neck has a sleek ebony fingerboard with 22 extra jumbo frets, and Thin U Neck contour. Active EMG-81 and EMG-60 humbuckers (Duncan Alnicos on Faded Cherry Sunburst) give you plenty of power and note definition. Gold hardware (chrome on Faded Cherry Sunburst) adds a touch of refinement.",
                     price="$969.00", stringNum="", typeOfGuitar =guitar2)

session.add(electric5)
session.commit()

# http://www.guitarcenter.com/Gibson-Faded-SG-Special-Electric-Guitar-102935921-i1149235.gc
electric6 = guitarInfo(user_id=1, name="Gibson 2014 SG Special Electric Guitar Desert Burst Vintage Gloss", description="The Gibson 2014 SG Special Electric Guitar celebrates Gibson's 120th Anniversary in style. It has a solid mahogany body and a maple neck with a '60s slim profile. The 24-fret rosewood fingerboard has trapezoid inlays and sports a 120th Anniversary banner at the 12th fret. The headstock has 2014 on the back and a Special truss-rod cover to commemorate the anniversary year.",
                     price="$881.00", stringNum="6", typeOfGuitar =guitar2)

session.add(electric6)
session.commit()

# http://www.guitarcenter.com/B-C--Rich-Bich-Double-Neck-Electric-Guitar-108590928-i2861916.gc
electric7 = guitarInfo(user_id=1, name="B.C. Rich Bich Double Neck Electric Guitar Pearl White", description="If you're looking to conquer miles and miles of new sonic terrain, the 2012 Pearl White B.C. Rich Double Neck Bich delivers with maximum style and impact. Its bloodline can traced to the late '70s, early '80s era B.C. Rich Classic lineup, but make no mistake: this guitar is all business. Its form, function and tone-shaping abilities scream 'sophistication.'",
                     price="$999.99", stringNum="12", typeOfGuitar =guitar2)

session.add(electric7)
session.commit()

# http://www.guitarcenter.com/Jackson-JS22-7-Dinky-DKA-7-String-Electric-Guitar-108925553-i2991564.gc
electric8= guitarInfo(user_id=1, name="Jackson JS22-7 Dinky DKA 7-String Electric Guitar Satin Black", description="The Jackson JS22-7 DKA Dinky JS Series seven-string packs a huge punch for the price. It features an arch-top basswood body, bolt-on maple neck, 16-radius rosewood fingerboard with 24 jumbo frets and piranha inlays, 26.5 scale length, dual high-output Jackson humbucking pickups, single volume and tone controls, direct-mount hard-tail bridge and die-cast tuners.",
                     price="$199.99", stringNum="7", typeOfGuitar =guitar2)

session.add(electric8)
session.commit()


# http://www.guitarcenter.com/Ibanez-S5528LW-Prestige-S-Series-8-String-Electric-Guitar-110141637-i3598128.gc
electric9 = guitarInfo(user_id=1, name="Ibanez S5528LW Prestige S Series 8 String Electric Guitar Hazelnut Ale Brown", description="As the crown jewel of Ibanez, the Prestige line represents the passion and pride of Japanese luthiery. These guitars, produced exclusively in Japan, have earned worldwide acclaim and respect throughout the industry for their craftsmanship, quality, and innovation. Combine this with the legendary Ibanez S body style, and you have an instrument that defines the Ibanez mission of quality, innovation and design. The S5528LW 8-string features an exotic African black limba capped mahogany body and super-rigid Ibanez Ultra-8 neck constructed of five, glued, solid pieces of maple/wenge to accommodate 27 scale string tension, and maintain superior tone and sustain. Electronics include a pair of US made DiMarzio D Activator 8 high-output pickups for strong, percussive, low notes with balanced highs that cut without being piercing. A 5-way switch allows for a variety of tone options.",
                     price="$1,999.99", stringNum="8", typeOfGuitar =guitar2)

session.add(electric9)
session.commit()




# populate left-handed guitars into database
# typeOfGuitar = guitar3

# http://www.guitarcenter.com/Fender-Left-Handed-American-Deluxe-Stratocaster-Electric-Guitar-423686-i1519082.gc
left1 = guitarInfo(user_id=1, name="Fender Left-Handed American Deluxe Stratocaster Electric Guitar", description="The left-handed Fender American Deluxe Stratocaster has all the modern features today's guitarists demand in an electric guitar. The compound-radius fretboard encourages exhilaratingly effortless string bending anywhere along the neck. New Fender N3 noiseless pickups supercharge your sound with improved Stratocaster tones for sparkling bell-like chime with no hum. The American Deluxe Stratocaster has reconfigured S-1 switching that offers even more knockout tonal options. Other features include staggered locking tuners, a 2-point synchronized American Deluxe tremolo bridge with pop-in arm, and a beveled neck heel. Fender includes a molded Fender-exclusive SKB case with glass-reinforced latches and TSA locks, cable, and strap locks with the left-handed American Deluxe Stratocaster.",
                     price="$1,699.99", stringNum="6", typeOfGuitar =guitar3)

session.add(left1)
session.commit()

# http://www.guitarcenter.com/Ibanez-GRG120BDXL-Left-Handed-Electric-Guitar-107887234-i2479576.gc
left2 = guitarInfo(user_id=1, name="Ibanez GRG120BDXL Left-Handed Electric Guitar Black", description="The GRG120BDXL Left-Handed Electric Guitar is an irresistable bargain from Ibanez, featuring the playability, warranty, and set-up of their more expensive instruments, but at a rock bottom price. It's all about the neck and this guitar gets a super-fast one made from a single piece of maple with a radiused rosewood fingerboard and shark teeth inlays. Powerful Ibanez-designed humbuckers provide plenty of output and are perfect for getting overdriven sounds. The GRG120BDX also comes equipped with an upgraded FAT-6 tremolo bridge that'll inspire you while keeping everything in tune.",
                     price="$229.99", stringNum="6", typeOfGuitar =guitar3)

session.add(left2)
session.commit()

# http://www.guitarcenter.com/Gretsch-Guitars-G5420LH-Electromatic-Left-Handed-Hollowbody-Guitar-108090424-i2569568.gc
left3 = guitarInfo(user_id=1, name="Gretsch Guitars G5420LH Electromatic Left-Handed Hollowbody Guitar", description="When the Gretsch R&D team unearthed a Baldwin-era Filter'Tron pickup with knockout punch and phenomenal twang, they incorporated its DNA into dynamic Black Top Filter'Tron pickups, which now endow Electromatic hollow-body instruments such as the G5420T with an electrifying voice and identity.",
                     price="$799.99", stringNum="6", typeOfGuitar =guitar3)

session.add(left3)
session.commit()

# http://www.guitarcenter.com/Ibanez-RG450DXB-Left-Handed-Electric-Guitar-108589060-i2824693.gc
left4 = guitarInfo(user_id=1, name="Ibanez RG450DXB Left-Handed Electric Guitar White", description="The RG is the most recognizable and distinctive guitar in the Ibanez line. Three decades of metal have forged this high-performance machine, honing it for both speed and strength. This RG450DXL Left-Handed model has a basswood body and a Wizard III neck shape that offers maximum comfort and speed. Its fingerboard is rosewood with 24 jumbo frets for bigger note bends and it also comes with triple Ibanez INF pickups that are wired to a 5-way switch for a variety of coil combinations and sounds. An Edge-Zero tremolo bridge and Cosmo black hardware complete the list of hard-rockin' appointments.",
                     price="$449.99", stringNum="6", typeOfGuitar =guitar3)

session.add(left4)
session.commit()

# http://www.guitarcenter.com/Traveler-Guitar-Left-Handed-Speedster-Travel-Electric-Guitar-105326482-i1466293.gc
left5 = guitarInfo(user_id=1, name="Traveler Guitar Left-Handed Speedster Travel Electric Guitar Candy Apple Red", description="Traveler Guitar's Left-handed Speedster Electric Guitar signifies a design revolution in travel guitars because of its unique modern-retro look and detachable teardrop arm support while providing a full-scale neck. In addition to its compact size and portability, the Traveler Speedster is built for performance with a high-output dual-rail humbucker pickup, a unique roller-style bridge, and volume and tone controls. With the arm support detached for travel, the entire lefty guitar fits neatly inside a high-quality gig bag (included) and is small enough to stow in airline overhead compartments.",
                     price="$399.99", stringNum="6", typeOfGuitar =guitar3)

session.add(left5)
session.commit()












# populate ukuleles into database
# typeOfGuitar = guitar4

# http://www.guitarcenter.com/Epiphone-Les-Paul-Acoustic-Electric-Concert-Ukulele-Outfit-106503329-i1689585.gc
ukulele1 = guitarInfo(user_id=1, name="Epiphone Les Paul Acoustic-Electric Concert Ukulele Outfit", description="The Les Paul ukulele is made of mahogany with a flame maple veneer top. It has a concert-size body that's slightly larger and louder (with deeper tone) than a soprano ukulele. It accepts standard G, C, E, A tuning. The neck is also mahogany with a rosewood fretboard and a D-profile for smooth fingering.",
                     price="$129.00", stringNum="4",  typeOfGuitar =guitar4)

session.add(ukulele1)
session.commit()

# http://www.guitarcenter.com/Gretsch-Guitars-Root-Series-G9120-Tenor-Standard-Ukulele-107619140-i2370639.gc
ukulele2 = guitarInfo(user_id=1, name="Gretsch Guitars Root Series G9120 Tenor Standard Ukulele Mahogany", description="Gretsch is famous for guitars and drums, but were also known as one of the best manufacturers of ukuleles. The Gretsch G9120 Tenor Standard Ukulele marks the return of ukuleles to the Gretsch family. It features a laminated mahogany, tenor-sized body and 2-pc mahogany neck for excellent tone. The tenor has a larger body than a concert ukulele, having more volume and deeper bass tone. The easy-to-play Rosewood fingerboard has 19 frets with dot inlays and Grover Sta-Tite to keep notes in tune.",
                     price="$129.00", stringNum="4",  typeOfGuitar =guitar4)

session.add(ukulele2)
session.commit()

# http://www.guitarcenter.com/Luna-Guitars-Banjolele-8--Ukulele-110156668-i2458962.gc
ukulele3 = guitarInfo(user_id=1, name="Luna Guitars Banjolele 8inch Ukulele Tobacco Burst Ulu Design", description="The etched patterns on the back of Luna's banjoleles are a tribute to traditional Hawaiian quilt design. In the early 1800's, missionaries brought woven fabrics and steel needles and taught the Hawaiian people how to make patchwork quilts. But the Hawaiians made them uniquely their own. The designs were cut from one piece by folding fabric in the same way that you would fold paper to cut snowflakes and were based on the many plants that surrounded them. Luna has chosen the KALO (taro plant) as inspiration because this plant was a sacred and an essential part of early Hawaiian life.",
                     price="$199.00", stringNum="4",  typeOfGuitar =guitar4)

session.add(ukulele3)
session.commit()

# http://www.guitarcenter.com/Fender-Mino-Aka-Koa-Cutaway-Electric-Ukulele-108421298-i2731256.gc
ukulele4 = guitarInfo(user_id=1, name="Fender Mino'Aka Koa Cutaway Electric Ukulele Natural", description="Fender's delightful concert ukulele, the Mino'Aka (Hawaiian for 'smile'), now has a cutaway and onboard electronics so you can plug into your favorite amp and strum the South Sea nights away. Premium features include an all-koa body for lilting uke tone, aged body and fretboard binding, elegant acrylic abalone rosette, three-piece mahogany neck with Telecaster-style headstock, 19-fret rosewood fingerboard, high-gloss finish, Fishman Kula preamp/pickup system with built-in tuner, and Aquila Nylagut strings.",
                     price="$329.99", stringNum="4",  typeOfGuitar =guitar4)

session.add(ukulele4)
session.commit()












# populate acoustic bass guitars into database
# typeOfGuitar = guitar5

# http://www.guitarcenter.com/Kala-Solid-Top-Fretless-Acoustic-Electric-U-BASS-109314864-i2999514.gc
abass1 = guitarInfo(user_id=1, name="Kala Solid Top Fretless Acoustic Electric U-BASS Natural", description="For the Kala U-BASS player, Kala offers additional visual options and adds a mid-range punch with the Solid spruce top U-BASS with mahogany back and sides. Since 2008, the U-BASS is still grabbing ears and turning heads. Praised for its colossal low end the acoustic-electric U-BASS features a new custom-designed shadow pickup system to dial in sonic boom.",
                     price="$449.00", stringNum="4",  typeOfGuitar =guitar5)

session.add(abass1)
session.commit()

# http://www.guitarcenter.com/Ibanez-AEB20E-Acoustic-Electric-Bass-Guitar-110466943-i3760955.gc
abass2= guitarInfo(user_id=1, name="Ibanez AEB20E Acoustic-Electric Bass Guitar Transparent Black Sunburst", description="The Ibanez AEB20E acoustic-electric bass features all of the same components of its cousin, the AEB10E but with a few minor differences. The AEB20E features a flamed sycamore top, mahogany back and sides, rosewood fretboard and bridge, 32inch scale, abalone rosette, chrome die-cast tuners, Ibanez AEQ-SP2 preamp with onboard tuner, and transparent black sunburst gloss finish.",
                     price="$399.99", stringNum="4",  typeOfGuitar =guitar5)

session.add(abass2)
session.commit()

# http://www.guitarcenter.com/Fender-T-Bucket-Grand-Concert-Acoustic-Electric-Bass-108746793-i2939146.gc
abass3= guitarInfo(user_id=1, name="Fender T-Bucket Grand Concert Acoustic-Electric Bass 3-Color Sunburst", description="The T-Bucket Bass E acoustic bass guitar is even more supercharged now, with upgraded features including a remarkable new holographic rosette inlay, new 12th-fret 'F' logo inlay design.",
                     price="$399.99", stringNum="4",  typeOfGuitar =guitar5)

session.add(abass3)
session.commit()

# http://www.guitarcenter.com/Traveler-Guitar-Ultra-Light-5-String-Acoustic-Electric-Travel-Bass-Guitar-110726312-i3923553.gc
abass4= guitarInfo(user_id=1, name="Traveler Guitar Ultra-Light 5-String Acoustic-Electric Travel Bass Guitar Natural", description="Weighing just 3 pounds 15 ounces and measuring only 33 in length, this 30-scale 5-string acoustic electric bass can go anywhere you want to take it. The Ultra-Light Bass 5-String features a custom piezo pickup so you can plug into your favorite amplifier, while the built-in thumb rest and removable lap-rest frame allow you play in comfort, even in the tightest of spaces.",
                     price="$449.99", stringNum="5",  typeOfGuitar =guitar5)

session.add(abass4)
session.commit()

# http://www.guitarcenter.com/Godin-A4-Ultra-Natural-Fretless-SA-Acoustic-Electric-Bass-Guitar-430656-i1535477.gc
abass5= guitarInfo(user_id=1, name="Godin A4 Ultra Natural Fretless SA Acoustic-Electric Bass Guitar Natural Ebony Fretboard", description="This Godin A4 SA fretless bass features endless sonic possibilities brought to you by Custom Godin electronics. It comes equipped with individual saddle transducers at the bridge and a 13-pin connector for direct control of Roland GR Series and Axon AX100 guitar synths. The Godin bass features a solid spruce top, for balanced sound reproduction. The silver leaf maple body adds strength and clarity to the A4 bass's sound. The rock maple neck adds plenty of sustain and definition from note to note. The soft C neck, cutaway on the Godin A4 SA fretless bass's upper bout, and 16inch radius add comfort for intricate progressions.",
                     price="$1,245.00", stringNum="4",  typeOfGuitar =guitar5)

session.add(abass5)
session.commit()













# populate electric bass guitars into database
# typeOfGuitar = guitar6

# http://www.guitarcenter.com/Fender-American-Deluxe-Jazz-Bass-V-5-String-Electric-Bass-105913719-i1520297.gc
ebass1= guitarInfo(user_id=1, name="Fender American Deluxe Jazz Bass V 5-String Electric Bass", description="The 5-string Fender American Deluxe Jazz Bass V delivers the modern features that bassists demand in a sleek, familiar electric bass design. An updated preamp circuit brings deeply exhilarating active and passive tone. Powerful-yet-quiet N3 Noiseless pickups present more clean headroom, extended EQ range, and tighter low-end response. The tonal options are vast, thanks to the active/passive toggle switch and passive tone control. These amazing electronics effortlessly handle the low B string with impeccable tone and seismic power. The classic Jazz Bass block fretboard inlays and binding present the Fender American Deluxe V bass in a rightfully classy light.",
                     price="$1,799.99", stringNum="5",  typeOfGuitar =guitar6)

session.add(ebass1)
session.commit()

# http://www.guitarcenter.com/Schecter-Guitar-Research-Stiletto-Studio-5-Bass-101765410-i1147992.gc
ebass2= guitarInfo(user_id=1, name="Schecter Guitar Research Stiletto Studio-5 Bass", description="The elegant Schecter Stiletto Studio-5 Bass pulls out all the stops with neck-thru-body, multilaminate construction and high-end appointments. It features a mahogany and bubinga body, multilaminate maple and walnut neck, and rosewood fingerboard with 24 jumbo frets and offset dot inlays. Also features a Diamond Custom bridge, Grover tuners, EMG-HZ pickups, 3-band EQ, master volume and blend controls, and satin gold hardware.",
                     price="$749.00", stringNum="5",  typeOfGuitar =guitar6)

session.add(ebass2)
session.commit()

# http://www.guitarcenter.com/Rogue-VB100-Violin-Bass-Guitar-109998849-i1532863.gc
ebass3= guitarInfo(user_id=1, name="Rogue VB100 Violin Bass Guitar Vintage Sunburst", description="The Rogue VB-100 violin bass guitar features a flamed maple arched top and back with the European-style hollowbody that makes it lightweight and capable of deep, resonant bass tones. The violin bass's traditional 31inch scale offers immediate familiarity in your hands. A custom trapeze tailpiece, pearloid pickguard, and body binding on front and back are added touches. Don't be fooled by the tiny price; this Rogue a serious violin bass nicely made with all the playability and tone of the original at a fraction of the cost.",
                     price="$219.99", stringNum="4",  typeOfGuitar =guitar6)

session.add(ebass3)
session.commit()

# http://www.guitarcenter.com/Epiphone-Thunderbird-Pro-IV-Bass-105334650-i1460863.gc
ebass4= guitarInfo(user_id=1, name="Epiphone Thunderbird Pro-IV Bass", description="The Epiphone Thunderbird Pro-IV bass builds on the illustrious history of the Thunderbird bass. This distinctively shaped rock-and-roll bass combines traditional design elements with new technology at a price any bassist can afford.",
                     price="$499.00", stringNum="4",  typeOfGuitar =guitar6)

session.add(ebass4)
session.commit()

# http://www.guitarcenter.com/Ibanez-SR506-Soundgear-6-String-102577814-i1732463.gc
ebass5= guitarInfo(user_id=1, name="Ibanez SR506 Soundgear 6-String Brown Mahogany Rosewood Fretboard", description="The Ibanez SR506 Bass is an incredibly well-crafted and equipped bass for its price. It features a slim, fast SR6 5-piece jatoba and bubinga neck on a sculpted mahogany body. The rosewood fretboard is fitted with medium frets and has oval abalone markers. Equipped with a B106 bridge 2 Bartonlini MK1-6 pickups that integrate perfectly with the active Bartolini MK1 3-band EQ. It's a bass that will excel in any style of music.",
                     price="$699.99", stringNum="6",  typeOfGuitar =guitar6)

session.add(ebass5)
session.commit()







# populate upright bass guitars into database
# typeOfGuitar = guitar7

# http://www.guitarcenter.com/Palatino-VE-550-Electric-Upright-Bass-109456475-i1170393.gc
ubass1 = guitarInfo(user_id=1, name="Palatino VE-550 Electric Upright Bass", description="The Palatino VE-550 Electric Upright Bass is the answer to many a bass player's prayers. With sweet sound, great looks, and light, portable design, the VE-550 bass has a chambered body of select spruce. The slim, maple neck and curved ebony fingerboard emulate an acoustic upright bass. The Palatino VE-550 bass's adjustable maple bridge rests on the piezo transducer pickup, giving the VE-550 electric upright its large, booming tone.",
                     price="$839.99", stringNum="4",  typeOfGuitar =guitar7)

session.add(ubass1)
session.commit()

# http://www.guitarcenter.com/NS-Design-NXT-4-String-Electric-Double-Bass-423893-i1524021.gc
ubass2= guitarInfo(user_id=1, name="NS Design NXT 4-String Electric Double Bass", description="he NXT Series Double Bass opens up a new horizon for the serious bassist looking to play a great instrument on a limited budget. These new instruments, crafted in the Czech Republic by the makers of the renowned CR Series, exemplify flawless workmanship at an incredible value. ",
                     price="$1,499.00", stringNum="4",  typeOfGuitar =guitar7)

session.add(ubass2)
session.commit()

# http://www.guitarcenter.com/Yamaha-SV-255-SV-Pro-5-String-Silent-Violin-106905078-i3973860.gc
ubass3 = guitarInfo(user_id=1, name="Yamaha SV-255 SV Pro 5-String Silent Violin", description="Some crazzzzy stuff maaan",
                     price="$1,845.00", stringNum="4",  typeOfGuitar =guitar7)

session.add(ubass3)
session.commit()

print "added guitars to db!"