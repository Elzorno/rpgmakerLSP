/*:
 * @target MZ
 * @plugindesc Places side-view party battlers on the right side of the battle field.
 * @author Codex
 *
 * @help
 * Moves actor battler home positions from RPG Maker MZ's default 816px-era
 * coordinates into the right side of this project's wider battle window.
 */

(() => {
    "use strict";

    const partySize = () => {
        if (!$gameParty) {
            return 4;
        }
        const members = $gameParty.battleMembers();
        return Math.max(1, members.length || $gameParty.maxBattleMembers());
    };

    Sprite_Actor.prototype.setActorHome = function(index) {
        const width = Graphics.boxWidth;
        const height = Graphics.boxHeight;
        const count = partySize();
        const centerIndex = (count - 1) / 2;
        const baseX = width * 0.78;
        const baseY = height * 0.5;
        const stepX = Math.min(44, width * 0.025);
        const stepY = Math.min(72, height * 0.065);

        this.setHome(
            Math.round(baseX + index * stepX),
            Math.round(baseY + (index - centerIndex) * stepY)
        );
    };
})();
