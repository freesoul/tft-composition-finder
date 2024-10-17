# TFT composition finder

## Available sets
The following sets come with default config and constants. To use another thant he last, the file `sets/__init__.py` has to be changed. You may do a pull request to change this to a config.
- Set 12 (current)
- Set 9
  
## Example usage (set 9)
  
```
python python -m  tft_composition_finder.cli --include-champs "Sett,Kog'maw,Illaoi,Lee Sin"  --emblems mythic_1,duelist_1
```  
  
Output:  
  
```
Composition: Azir,Illaoi,Janna,Kog'maw,Lee Sin,Lillia,Sett,Syndra - Score 17.0 - Cost 28 - invoker 4,mythic 3,dragonlord 2,warden 2,arcanist 2,duelist 2
Composition: Alune,Illaoi,Janna,Kog'maw,Lee Sin,Lillia,Sett,Syndra - Score 18.4 - Cost 26 - invoker 4,mythic 3,umbral 2,dragonlord 2,warden 2,arcanist 2,duelist 2
Composition: Annie,Illaoi,Janna,Kog'maw,Lee Sin,Lillia,Sett,Syndra - Score 17.0 - Cost 27 - invoker 4,mythic 3,dragonlord 2,warden 2,arcanist 2,duelist 2
Composition: Illaoi,Janna,Kog'maw,Lee Sin,Qiyana,Sett,Syndra,Volibear - Score 12.8 - Cost 24 - duelist 4,dragonlord 2,invoker 2,warden 2,arcanist 2
Composition: Illaoi,Irelia,Janna,Kog'maw,Lee Sin,Qiyana,Sett,Syndra - Score 12.8 - Cost 26 - duelist 4,dragonlord 2,invoker 2,warden 2,arcanist 2
Composition: Illaoi,Janna,Kog'maw,Lee Sin,Qiyana,Sett,Syndra,Tristana - Score 11.8 - Cost 24 - duelist 4,dragonlord 2,invoker 2,warden 2,arcanist 2
Composition: Diana,Illaoi,Janna,Kog'maw,Lee Sin,Sett,Syndra,Xayah - Score 16.0 - Cost 27 - dragonlord 4,invoker 2,warden 2,arcanist 2,duelist 2,lovers 1
Composition: Illaoi,Janna,Kog'maw,Lee Sin,Rakan,Sett,Syndra,Xayah - Score 17.0 - Cost 29 - dragonlord 4,invoker 2,warden 2,arcanist 2,duelist 2,lovers 1
Composition: Illaoi,Irelia,Janna,Kog'maw,Lee Sin,Sett,Syndra,Volibear - Score 12.8 - Cost 27 - duelist 4,dragonlord 2,invoker 2,warden 2,arcanist 2
Composition: Illaoi,Janna,Kog'maw,Lee Sin,Sett,Syndra,Tristana,Volibear - Score 11.8 - Cost 25 - duelist 4,dragonlord 2,invoker 2,warden 2,arcanist 2
Composition: Illaoi,Janna,Kog'maw,Lee Sin,Neeko,Sett,Syndra,Zoe - Score 15.0 - Cost 24 - arcanist 4,mythic 3,dragonlord 2,invoker 2,warden 2,duelist 2
Composition: Amumu,Gnar,Illaoi,Janna,Kog'maw,Lee Sin,Sett,Syndra - Score 14.0 - Cost 24 - warden 4,dragonlord 2,invoker 2,arcanist 2,duelist 2
Composition: Gnar,Illaoi,Janna,Kog'maw,Lee Sin,Nautilus,Sett,Syndra - Score 17.0 - Cost 25 - warden 4,mythic 3,dragonlord 2,invoker 2,arcanist 2,duelist 2
Composition: Alune,Annie,Illaoi,Janna,Kog'maw,Lee Sin,Sett,Syndra - Score 15.4 - Cost 26 - invoker 4,umbral 2,dragonlord 2,warden 2,arcanist 2,duelist 2
Composition: Annie,Azir,Illaoi,Janna,Kog'maw,Lee Sin,Sett,Syndra - Score 14.0 - Cost 28 - invoker 4,dragonlord 2,warden 2,arcanist 2,duelist 2
Composition: Alune,Illaoi,Kog'maw,Lee Sin,Neeko,Sett,Syndra,Zoe - Score 14.4 - Cost 25 - arcanist 4,mythic 3,umbral 2,invoker 2,warden 2,duelist 2
Composition: Illaoi,Kog'maw,Lee Sin,Neeko,Rakan,Sett,Syndra,Zoe - Score 15.0 - Cost 27 - arcanist 4,mythic 3,warden 2,dragonlord 2,duelist 2,lovers 1
Composition: Illaoi,Kindred,Kog'maw,Lee Sin,Neeko,Sett,Syndra,Zoe - Score 14.6 - Cost 24 - arcanist 4,fated 3,mythic 3,warden 2,duelist 2
Composition: Aphelios,Illaoi,Kog'maw,Lee Sin,Neeko,Sett,Syndra,Zoe - Score 16.0 - Cost 25 - arcanist 4,mythic 3,fated 3,warden 2,sniper 2,duelist 2
Composition: Illaoi,Kog'maw,Lee Sin,Neeko,Sett,Syndra,Wukong,Zoe - Score 15.2 - Cost 27 - arcanist 4,mythic 3,heavenly 2,warden 2,duelist 2,great 1
Composition: Amumu,Illaoi,Kog'maw,Lee Sin,Nautilus,Sett,Syndra,Thresh - Score 16.6 - Cost 27 - warden 4,mythic 3,fated 3,arcanist 2,duelist 2
Composition: Gnar,Illaoi,Kog'maw,Lee Sin,Nautilus,Sett,Syndra,Thresh - Score 16.6 - Cost 26 - warden 4,mythic 3,fated 3,arcanist 2,duelist 2
Composition: Aphelios,Gnar,Illaoi,Kog'maw,Lee Sin,Nautilus,Sett,Syndra - Score 18.0 - Cost 26 - warden 4,fated 3,mythic 3,sniper 2,arcanist 2,duelist 2
Composition: Gnar,Illaoi,Kindred,Kog'maw,Lee Sin,Nautilus,Sett,Syndra - Score 18.6 - Cost 25 - warden 4,fated 3,mythic 3,dryad 2,arcanist 2,duelist 2
Composition: Azir,Gnar,Illaoi,Kog'maw,Lee Sin,Nautilus,Sett,Syndra - Score 17.0 - Cost 28 - warden 4,mythic 3,dryad 2,invoker 2,arcanist 2,duelist 2
Composition: Gnar,Illaoi,Kog'maw,Lee Sin,Nautilus,Sett,Syndra,Xayah - Score 17.0 - Cost 28 - warden 4,mythic 3,dragonlord 2,arcanist 2,duelist 2,lovers 1
Composition: Gnar,Illaoi,Kog'maw,Lee Sin,Nautilus,Rakan,Sett,Syndra - Score 17.0 - Cost 28 - warden 4,mythic 3,dragonlord 2,arcanist 2,duelist 2,lovers 1
Composition: Amumu,Aphelios,Illaoi,Kog'maw,Lee Sin,Nautilus,Sett,Syndra - Score 18.0 - Cost 27 - warden 4,mythic 3,fated 3,sniper 2,arcanist 2,duelist 2
Composition: Alune,Illaoi,Janna,Kog'maw,Lee Sin,Lillia,Sett,Udyr - Score 17.9 - Cost 27 - invoker 4,mythic 3,umbral 2,dragonlord 2,warden 2,duelist 2,spirit walker 1
Composition: Hwei,Illaoi,Kog'maw,Lee Sin,Lillia,Neeko,Sett,Udyr - Score 18.5 - Cost 29 - mythic 5,invoker 2,arcanist 2,warden 2,duelist 2,artist 1,spirit walker 1
Composition: Aphelios,Gnar,Illaoi,Kindred,Kog'maw,Lee Sin,Nautilus,Sett - Score 17.5 - Cost 24 - warden 4,mythic 3,fated 3,dryad 2,sniper 2,duelist 2
Composition: Hwei,Illaoi,Janna,Kog'maw,Lee Sin,Nautilus,Neeko,Sett - Score 18.5 - Cost 26 - mythic 5,warden 2,dragonlord 2,invoker 2,arcanist 2,duelist 2,artist 1
Composition: Hwei,Illaoi,Kog'maw,Lee Sin,Nautilus,Neeko,Rakan,Sett - Score 18.5 - Cost 29 - mythic 5,warden 2,arcanist 2,dragonlord 2,duelist 2,artist 1,lovers 1
Composition: Hwei,Illaoi,Kog'maw,Lee Sin,Nautilus,Neeko,Sett,Wukong - Score 18.7 - Cost 29 - mythic 5,warden 2,heavenly 2,arcanist 2,duelist 2,great 1,artist 1
Composition: Alune,Hwei,Illaoi,Kog'maw,Lee Sin,Nautilus,Neeko,Sett - Score 17.9 - Cost 27 - mythic 5,warden 2,umbral 2,invoker 2,arcanist 2,duelist 2,artist 1
Composition: Hwei,Illaoi,Kog'maw,Lee Sin,Nautilus,Neeko,Sett,Xayah - Score 18.5 - Cost 29 - mythic 5,warden 2,dragonlord 2,arcanist 2,duelist 2,lovers 1,artist 1
Composition: Illaoi,Kog'maw,Lee Sin,Lillia,Nautilus,Neeko,Sett,Xayah - Score 18.5 - Cost 28 - mythic 5,warden 2,dragonlord 2,invoker 2,arcanist 2,duelist 2,lovers 1
Composition: Amumu,Illaoi,Janna,Kog'maw,Lee Sin,Lissandra,Nautilus,Sett - Score 19.5 - Cost 27 - warden 4,mythic 3,dragonlord 2,invoker 2,porcelain 2,arcanist 2,duelist 2
Composition: Amumu,Illaoi,Kog'maw,Lee Sin,Lissandra,Nautilus,Sett,Xayah - Score 19.5 - Cost 30 - warden 4,mythic 3,dragonlord 2,porcelain 2,arcanist 2,duelist 2,lovers 1
Composition: Alune,Amumu,Illaoi,Kog'maw,Lee Sin,Lissandra,Nautilus,Sett - Score 18.9 - Cost 28 - warden 4,mythic 3,umbral 2,invoker 2,porcelain 2,arcanist 2,duelist 2
Composition: Amumu,Illaoi,Kog'maw,Lee Sin,Lissandra,Nautilus,Rakan,Sett - Score 19.5 - Cost 30 - warden 4,mythic 3,porcelain 2,arcanist 2,dragonlord 2,duelist 2,lovers 1
Composition: Illaoi,Kog'maw,Lee Sin,Lillia,Nautilus,Neeko,Sett,Wukong - Score 18.7 - Cost 28 - mythic 5,warden 2,heavenly 2,invoker 2,arcanist 2,duelist 2,great 1
Composition: Alune,Illaoi,Janna,Kog'maw,Lee Sin,Lillia,Lissandra,Sett - Score 18.9 - Cost 27 - invoker 4,mythic 3,umbral 2,dragonlord 2,arcanist 2,warden 2,duelist 2
Composition: Hwei,Illaoi,Kog'maw,Lee Sin,Lillia,Neeko,Sett,Wukong - Score 20.7 - Cost 29 - mythic 5,heavenly 2,invoker 2,arcanist 2,warden 2,duelist 2,great 1,artist 1
Composition: Illaoi,Kog'maw,Lee Sin,Lillia,Neeko,Sett,Tahm Kench,Wukong - Score 18.7 - Cost 27 - mythic 5,heavenly 2,invoker 2,arcanist 2,warden 2,duelist 2,great 1
Composition: Alune,Illaoi,Janna,Kog'maw,Lee Sin,Lillia,Sett,Xayah - Score 18.9 - Cost 27 - invoker 4,dragonlord 3,mythic 3,umbral 2,warden 2,duelist 2,lovers 1
Composition: Hwei,Illaoi,Kog'maw,Lee Sin,Lillia,Neeko,Rakan,Sett - Score 20.5 - Cost 29 - mythic 5,arcanist 2,dragonlord 2,warden 2,invoker 2,duelist 2,artist 1,lovers 1
Composition: Hwei,Illaoi,Kog'maw,Lee Sin,Lillia,Neeko,Sett,Soraka - Score 19.0 - Cost 27 - mythic 5,invoker 2,heavenly 2,arcanist 2,warden 2,duelist 2,artist 1
Composition: Hwei,Illaoi,Kog'maw,Lee Sin,Lillia,Neeko,Sett,Xayah - Score 20.5 - Cost 29 - mythic 5,dragonlord 2,invoker 2,arcanist 2,warden 2,duelist 2,lovers 1,artist 1

Done. Best compositions:
Composition: Hwei,Illaoi,Kog'maw,Lee Sin,Lillia,Neeko,Sett,Wukong - Score 20.7 - Cost 29 - mythic 5,heavenly 2,invoker 2,arcanist 2,warden 2,duelist 2,great 1,artist 1
Composition: Hwei,Illaoi,Kog'maw,Lee Sin,Lillia,Neeko,Rakan,Sett - Score 20.5 - Cost 29 - mythic 5,arcanist 2,dragonlord 2,warden 2,invoker 2,duelist 2,artist 1,lovers 1
Composition: Hwei,Illaoi,Kog'maw,Lee Sin,Lillia,Neeko,Sett,Xayah - Score 20.5 - Cost 29 - mythic 5,dragonlord 2,invoker 2,arcanist 2,warden 2,duelist 2,lovers 1,artist 1
Composition: Amumu,Illaoi,Janna,Kog'maw,Lee Sin,Lissandra,Nautilus,Sett - Score 19.5 - Cost 27 - warden 4,mythic 3,dragonlord 2,invoker 2,porcelain 2,arcanist 2,duelist 2
Composition: Amumu,Illaoi,Kog'maw,Lee Sin,Lissandra,Nautilus,Sett,Xayah - Score 19.5 - Cost 30 - warden 4,mythic 3,dragonlord 2,porcelain 2,arcanist 2,duelist 2,lovers 1
Composition: Amumu,Illaoi,Kog'maw,Lee Sin,Lissandra,Nautilus,Rakan,Sett - Score 19.5 - Cost 30 - warden 4,mythic 3,porcelain 2,arcanist 2,dragonlord 2,duelist 2,lovers 1
Composition: Hwei,Illaoi,Kog'maw,Lee Sin,Lillia,Neeko,Sett,Soraka - Score 19.0 - Cost 27 - mythic 5,invoker 2,heavenly 2,arcanist 2,warden 2,duelist 2,artist 1
Composition: Alune,Amumu,Illaoi,Kog'maw,Lee Sin,Lissandra,Nautilus,Sett - Score 18.9 - Cost 28 - warden 4,mythic 3,umbral 2,invoker 2,porcelain 2,arcanist 2,duelist 2
Composition: Alune,Illaoi,Janna,Kog'maw,Lee Sin,Lillia,Lissandra,Sett - Score 18.9 - Cost 27 - invoker 4,mythic 3,umbral 2,dragonlord 2,arcanist 2,warden 2,duelist 2
Composition: Alune,Illaoi,Janna,Kog'maw,Lee Sin,Lillia,Sett,Xayah - Score 18.9 - Cost 27 - invoker 4,dragonlord 3,mythic 3,umbral 2,warden 2,duelist 2,lovers 1
```

