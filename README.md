# Physical Hearthstone

> A somewhat faithful re-creation of Classic Hearthstone for the tabletop, made by oflords

## Changes Made

While I wanted to stay as faithful to the first version of Hearthstone, I also wanted to include some changes that make the game play better, include more memerable cards and overall be simpler for the tabletop. This does however come at the sacrifice of some cards and effects, if I missed your favourite you can always tweak this list.

### Card Pool Tweaks

* Murloc buffs only apply to the friendly murlocs.
    > This change was taken from patch 6.2.0.15181 and makes the game much easier to play when both players incorperate Murlocs.
* Card changes from patches 1.0.0.5314, 1.1.0.6024, 1.2.0.6485 and 2.0.0.7234 were applied.
    > Unleash the Hounds, Eaglehorn Bow, Leeroy Jenkins, Flare, Gadgetzan Auctioneer and Soulfire were all strong cards at release, so to make the game more approachable the overly tuned decks were adjusted.
* Starving Buzzard was tweaked to be a 4 mana 3/2.
    > It did get a nerf in patch 1.2.0.6485 that absolutely killed the card, so making the mana change be to 4 not 5 should allow the card to be in a better position, especially with Unleash the Hounds nerfed.
* Re-Worded Lorewalker Cho to "Whenever a player casts a spell, put it in the other players hand instead of discarding".
    > As there is no discard tutoring in Hearthstone, giving the player the card as played makes more sense.
* Renamed Ysera to "At the end of your turn, add a random unique Dream card to your hand".
    > Makes it so you cannot get a duplicate, needing for less cards printed. If you have all four in your hand, it does nothing.
* Changed Bane of Doom to summon a 4/5 Token with a Demon Counter instead of a random demon.
    > Random card effects mean either printing more cards or discounting some in use. I just averanged statlines, and sadly a 3.6~/5.1~ was impossible so I settled on 4/5.
* Summoned 1/1s, 2/1s and 2/2s will now be referred to as Tokens.
    > To avoid needing to print Snakes, Hounds, Treants, etc, those common summoned cards will now be tokens, which are generic cards taking the form of various amalgams with the required statlines. This helps clear confusion, streamline effects and require less overall cards to make the game work. The only downside to this approach is you do need tribe tokens so summoned beasts can still be targeted at the correct times, but I prefer the change.

### Card Pool Additions

* Potion of Polymorph
    > To ensure Mage has enough Secrets and seeing the removal of Mirror Entity, I added Potion of Polymorph as I feel it is a comparable effect. I also adjusted the rarity to Common to make it exactly take the slot.
* Fel Reaver
    > Needed something to fill the slot of a neutral epic and it was printed early enough and is a simple mechanic for the tabletop. Also has a similar swing effect as faceless.
* Loatheb
    > A popular card, released in the first card drop after the games launch. Also I wanted to play it.
* Reno Jackson
    > Highlander in classic might struggle a little, but could make for a fun time with a friend.
* Sir Finley Mrrgglton
    > Fun mechanic, iconic, the whole package.

### Card Pool Removals

* Faceless Manipulator
    > To avoid situations where copies of all cards are in use or using blank cards as fill ins, the exclusion of this card was in my mind justified.
* Mirror Entity
    > Same as Faceless Manipulator
* Nozdurmu
    > I thought about nerfing the effect to 30 seconds, but in a physical card game, there can be too many questions regarding if a move made was "legal", so putting the clock this heavily on players seems unfair and too annoying to deal with.
* Elite Tauren Chieftain
    > Needs a lot of special cards printed for an effect that was never super popular. No thank you.
* Geblin Mekkatorque
    > Too many cards, yuck.

## Priest Rework

While looking through cards to discard, Priest stuck out like a sore thumb in regards to work. It had a total of three cards that revolve around copying cards, something which I am trying to avoid. The cards in question that I removed are:

* Mind Vision
* Thoughtsteal
* Mindgames

To replace them, I have added:

* Scarlet Subjugator (Common)
* Thoughtsteal (Epic)
* Power Infusion (Basic)

### Creation Guide

1. Download or clone this repository and navigate to the JSON folder within.
2. Import the .hcards onto hearthcards.net and export them as .png
3. Place all the .png cards into a single folder, duplicating the files for each copy of the card you want
    1. 1x for class legendaries
    2. 2x for class cards & neutral legendaries
    3. 4x for neutrals
    4. tokens vary
4. Run the python script (install Python and run a console command to run the script) to generate a printable PDF
5. Take the PDF and print it with a printer or printing shop (I would suggest 210 glossy paper if possible as it makes colours vibrant and the cards themselves are thick)
6. Cut them out, TAKING AGES (try getting a paper trimmer if possible)
7. Put them in sleeves (solid backed works best, glossy eclipse pro works well)
8. Use Lotus app, random.org and counters for play
9. Enjoy
