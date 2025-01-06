1/1/2025

This is an attempt to create a chat program using nothing but a rudimentary knowledge of computer programming, configuration management, and testing.

Creating the first snippets of code is looking fairly straightforward.  Will debugging be as straightforward?  Only time will tell.

1/6/2026
OK, I need to write this part down to think it through... what is the order of operations for calculating a) PC/NPC's status, then b) calculate a combat action.

The foundation is:

- Basic raw stat / skill numbers 

	Raws can only update on specific events like levelling up
	Keep a log of these events for each toon, for troubleshooting
	- Stretch goal: If there are choices, construct a template that automatically updates when you ding
	Raws:
	- Stats 	(Strength, Intelligence, Wisdom, Dexterity, Constitution, Charisma,
					Quickness, Piety, Empathy, Vitality, Agility, Accuracy, Will, Fate)
	- Max 		(hit, magic, action, lungs?, spare2, spare3)
	- Regens	(hit, magic, action, lungs?, spare2, spare3)
	- Resists 	(Fire, Cold, Poison, Disease, Magic, 
					Electric, Acid, Force, Sonic, 
					Psychic, Sanity, Nature, Radiant, Arcane,
					Sleaze, Stench, Spooky, Life, Death, 
					Light, Dark, Shadow, Holy,
					Spirit, Body, Matter, Energy,
					Local1, Local2, Local3, Local4)
	- Criticals	(Melee, Range, Magic, Healing)
	- Faction (stretch)
	- Armor 	(piercing, crushing, slashing) 
	- Virtues	(Achievement, Charity, Compassion, Confidence, Determination, Discipline, 
					Diligence, Empathy, Faith, Fidelity, Forebearance, Fortitude, Friendliness, 
					Honesty, Honor, Hope, Humility, Idealism, Innocence, Justice, Liberality, 
					Loyalty, Magnificence, Magnanimity, Mercy, Modesty, Patience, Peristence, 
					Precision, Prudence, Sacrifice, Spiritedness, Spirituality, Temperance,  
					Valor, Wisdom, Wit, Zeal)

	Adjustment path: Effects adjust raws, raws adjust 

- Calculate adjustments based on Skills

	Skills can change just about any stat
	All skill adjustments are packed into a single structure
	- Stretch goal, "validate structure" which recalculates this structure based on skills

- Calculate adjustments based on Inventory
	- Stat 

(Updates when items are equipped and unequipped)

- Calculate adjustments based on Effects

Base stats should either be trimmed, or assigned "covariance" to represent their similarity
	- If you've worked one of these stats up to be max for your level, that contributes
		to the advancement of others
	- Why bother with the differences?  Well, different skills and abilities from different zones 
		could be tied to different 

Notes on Inventory items:
- Ideally, most inventory loot items would be generated a la Ultima Online, with randomized stat bonuses.
	- Like Soulash, these bonuses would be based somewhat on the zone's available materials
		and tagged accordingly.
	- Like WoW, they would be created at 6 levels of rarity / power: 
		- light grey, white, green, blue, purple, orange 
		- Each color is specifically tied to a level on the power curve, to control drop quality.
	- You have a couple of dozen resists.  
		- Any given zone will only challenge 4 of them.
		- Any given piece of armor will only protect against 6 of them.
- Players have "mannequins" which store your armor sets.  
	- You start with 5, and can gain a few as you level.
	- You also gain one special mannequin for each zone, which appears after a basic quest there
		that helps establish the lore for the zone.
		- This special mannequin tracks how many pieces of Legendary you've collected for that zone
	- Every zone will have a set of "Legendary armor" for your skillset, 
		- which is designed to be near-optimal for the zone, 
		- with exactly the right resists, for example.
		








