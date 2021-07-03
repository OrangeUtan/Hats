# Changelog

<!--next-version-placeholder-->

## v3.0.0 (2021-07-03)
### Feature
* Recipes for all glasses ([`483fc20`](https://github.com/OrangeUtan/Hats/commit/483fc20f562716a3a571c70b0aba23c515836bf4))
* Recipe for Feather Headband ([`ce72523`](https://github.com/OrangeUtan/Hats/commit/ce725232c401262589dadfabcd5e15bddc8562e9))
* Crafting recipes for toad hats ([`985b33c`](https://github.com/OrangeUtan/Hats/commit/985b33cbcafd033d705a22a6025f5bbda3fcd93e))
* Hat loot tables no longer grouped by category ([`bd2831f`](https://github.com/OrangeUtan/Hats/commit/bd2831fa68a5ff96957e9ed6f3d3f7b7660a9c74))

### Fix
* Load function not executed ([`dc2fc3a`](https://github.com/OrangeUtan/Hats/commit/dc2fc3a11dbb2db702844901c03941ec886f7938))
* Yellow shulker box method not working ([`0b07bfd`](https://github.com/OrangeUtan/Hats/commit/0b07bfd244539148496eaf3a44c92e09aac99fc3))
* Renamed "native_american_headband" to "feather headband" ([`3d06f2e`](https://github.com/OrangeUtan/Hats/commit/3d06f2e3ddab081734be432f1bd4918d03374ab9))
* Resourcepack didn't display hats if built from cache ([`1e74309`](https://github.com/OrangeUtan/Hats/commit/1e74309d15f6fa290b3c3903c924c1e93d893007))
* Changed 3D glasses type to "three_d_glass" ([`bedf278`](https://github.com/OrangeUtan/Hats/commit/bedf278d59cfde30acb40b8dc04722bd01fbfedf))
* Rainbow glasses was not displayed ([`47c8ffa`](https://github.com/OrangeUtan/Hats/commit/47c8ffa1d0c44577f9d1da7573b73fc6fd2b4644))

### Breaking
* Renemad type of squid to posh_squid  ([`1bcf7c9`](https://github.com/OrangeUtan/Hats/commit/1bcf7c960953f45434b8d94c7459d84d2dcdb448))

## [2.3.1] - 2020-06-17
### Added
- Configuration book
#### Hats
- `dog`
- `earth`

### Internal
#### Added
- Install function
- Ability to add custom loot to chests
#### Changed
- Using mcanitexgen to generate texture animations
- Advancements now query for hat type NBT tag instead of Custom Model Data
#### Removed
- Removed **is_hat** tag from all hats

## [2.3.0] - 2020-05-27
### Added
- Villager profession trades
- Wandering Trader now can have a favorite cat
- German translation
- Added some lore to hats
- Removing storage and advancements on uninstall

### Changed
- Villagers favorite cats are now dependent on biome
- Zombies only get dressed with Jason Mask at around midnight
- Wiggly Ghasts can only be found in mansions at night
#### Performance
- Only mobs near player get dressed
- Scheduling functions in different intervals instead of using **tick.mcfunction**
- Using shulkerbox method for hat mechanic
- Using advancements to trigger hat mechanic
- Replaced some NBT selectors

### Removed
- **fix_hat/...** functions. Replaced with shulkerbox method

### Fixed
- Villagers were dressed with wrong hat item

### Internal
#### Added
- Central hat registry for code generation
#### Changed
- Using predicates for randomnes and checks
- Using loot tables for random trade prices
- Generating item models for hats
- Generating hat loot tables
- Generating **_all** and **_rand** category loot tables

## [2.2.1] - 2020-05-17

### Internal
#### Added
- Github Action to create releases
#### Changed
- Combined hats resourcepack and datapack into one repository

## [2.2.0] - 2019-10-29
### Added
- `Wiggly Ghast` hat
- `Native American Headband` hat
- `Jason Mask`
- Dressing Zombie Pigmans
- Zombies can be dressed with Jason Mask
- Loot tables for all hats

### Removed
- **/equip** and **/give** functions. Use loot tables instead
- Removed **give_all_...** function tags

### Fixed
- `Arrow` and `Red Snorkel Mask` were not displaying on players head

### Internal
#### Added
- Added Item tags for the items used as hats
- Added **is_hat**, **hats.hat** and hat type NBT tags to all hats. Gives more information than just the Custom Model Data
- Added **_all** and **_rand** loot tables for each categories
#### Changed
- Using loot tables instead of functions for hat behaviour (equip, give, etc.)
- Using the new hat loot tables for dressing and trades
- Using **hats.mob.dont_dress** instead of **hats_is_dressed** tag to indicate mob is already dressed

## [2.1.0] - 2019-10-10
### Added
- Special trades for armorer, librarian and toolsmith villagers
- Dressing Wandering Trader
- Function tags to receive all hats for each category
#### Hats
- `Frying pan`
- `Luigi` and `Mario`
- `Mario Cap`, `Luigi Cap` and `Cappy`
- `Toad Blue`, `Toad Green`, `Toad Red` and `Toad Yellow`
- `Armorer`
- `Farmer`
- `Villager Nose`
- `Tophat with Monocle`

### Changed
- Renamed hat **glasses/3D** to **glasses/three_d**

### Internal
- Using loot tables instead of functions to dress mobs
