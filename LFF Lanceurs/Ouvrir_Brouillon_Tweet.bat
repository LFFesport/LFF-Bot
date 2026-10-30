@echo off
echo ========================================================
echo   Ligue Francaise de Fortnite (LFF) - Twitter/X Bot
echo ========================================================
echo Generation du brouillon de tweet LFF...
cd /d "%~dp0.."
python "LFF Scripts\lff_twitter_bot.py" --draft-ranking
exit
