/*****************************************************************************
* Model: game.qm
* File:  ././mine1.c
*
* This file has been generated automatically by QP Modeler (QM).
* DO NOT EDIT THIS FILE MANUALLY.
*
* Please visit www.state-machine.com/qm for more information.
*****************************************************************************/
#include "qp_port.h"
#include "bsp.h"
#include "game.h"

Q_DEFINE_THIS_FILE

/* encapsulated delcaration of the Mine1 HSM -------------------------------*/
/* @(/2/3) .................................................................*/
/** 
* The Mine1 orthogonal component
*/
typedef struct Mine1Tag {
/* protected: */
    QHsm super;

/* private: */
    uint8_t x;
    uint8_t y;

/* public: */
    uint8_t exp_ctr;
} Mine1;

/* protected: */
static QState Mine1_initial(Mine1 * const me, QEvt const * const e);
static QState Mine1_unused(Mine1 * const me, QEvt const * const e);
static QState Mine1_used(Mine1 * const me, QEvt const * const e);
static QState Mine1_exploding(Mine1 * const me, QEvt const * const e);
static QState Mine1_planted(Mine1 * const me, QEvt const * const e);


/* local objects -----------------------------------------------------------*/
static Mine1 l_mine1[GAME_MINES_MAX];             /* a pool of type-1 mines */

                             /* helper macro to provide the ID of this mine */
#define MINE_ID(me_)    ((uint8_t)((me_) - l_mine1))

/* Mine1 class definition --------------------------------------------------*/
/* @(/2/12) ................................................................*/
QHsm * Mine1_ctor(uint8_t id) {
    Mine1 *me;
    Q_REQUIRE(id < GAME_MINES_MAX);
    me = &l_mine1[id];
    /* superclass' ctor */
    QHsm_ctor(&me->super, (QStateHandler)&Mine1_initial);
    return (QHsm *)me;
}
/* @(/2/3) .................................................................*/
/* @(/2/3/3) ...............................................................*/
/* @(/2/3/3/0) */
static QState Mine1_initial(Mine1 * const me, QEvt const * const e) {
    static uint8_t dict_sent;

    if (!dict_sent) {
        QS_OBJ_DICTIONARY(&l_mine1[0]); /* obj. dictionaries for Mine1 pool */
        QS_OBJ_DICTIONARY(&l_mine1[1]);
        QS_OBJ_DICTIONARY(&l_mine1[2]);
        QS_OBJ_DICTIONARY(&l_mine1[3]);
        QS_OBJ_DICTIONARY(&l_mine1[4]);

        QS_FUN_DICTIONARY(&Mine1_initial);/*fun. dictionaries for Mine1 HSM */
        QS_FUN_DICTIONARY(&Mine1_unused);
        QS_FUN_DICTIONARY(&Mine1_used);
        QS_FUN_DICTIONARY(&Mine1_planted);
        QS_FUN_DICTIONARY(&Mine1_exploding);

        dict_sent = 1U;
    }
    /* local signals */
    QS_SIG_DICTIONARY(MINE_PLANT_SIG,    me);
    QS_SIG_DICTIONARY(MINE_DISABLED_SIG, me);
    QS_SIG_DICTIONARY(MINE_RECYCLE_SIG,  me);
    QS_SIG_DICTIONARY(SHIP_IMG_SIG,      me);
    QS_SIG_DICTIONARY(MISSILE_IMG_SIG,   me);

    (void)e; /* avoid the "unreferenced parameter" warning */
    return Q_TRAN(&Mine1_unused);
}
/* @(/2/3/3/1) .............................................................*/
static QState Mine1_unused(Mine1 * const me, QEvt const * const e) {
    QState status;
    switch (e->sig) {
        /* @(/2/3/3/1/0) */
        case MINE_PLANT_SIG: {
            me->x = Q_EVT_CAST(ObjectPosEvt)->x;
            me->y = Q_EVT_CAST(ObjectPosEvt)->y;
            status = Q_TRAN(&Mine1_planted);
            break;
        }
        default: {
            status = Q_SUPER(&QHsm_top);
            break;
        }
    }
    return status;
}
/* @(/2/3/3/2) .............................................................*/
static QState Mine1_used(Mine1 * const me, QEvt const * const e) {
    QState status;
    switch (e->sig) {
        /* @(/2/3/3/2) */
        case Q_EXIT_SIG: {
            /* tell the Tunnel that this mine is becoming disabled */
            MineEvt *mev = Q_NEW(MineEvt, MINE_DISABLED_SIG);
            mev->id = MINE_ID(me);
            QACTIVE_POST(AO_Tunnel, (QEvt *)mev, me);
            status = Q_HANDLED();
            break;
        }
        /* @(/2/3/3/2/0) */
        case MINE_RECYCLE_SIG: {
            status = Q_TRAN(&Mine1_unused);
            break;
        }
        default: {
            status = Q_SUPER(&QHsm_top);
            break;
        }
    }
    return status;
}
/* @(/2/3/3/2/1) ...........................................................*/
static QState Mine1_exploding(Mine1 * const me, QEvt const * const e) {
    QState status;
    switch (e->sig) {
        /* @(/2/3/3/2/1) */
        case Q_ENTRY_SIG: {
            me->exp_ctr = 0U;
            status = Q_HANDLED();
            break;
        }
        /* @(/2/3/3/2/1/0) */
        case TIME_TICK_SIG: {
            /* @(/2/3/3/2/1/0/0) */
            if ((me->x >= GAME_SPEED_X) && (me->exp_ctr < 15)) {
                ObjectImageEvt *oie;
                ++me->exp_ctr;  /* advance the explosion counter */
                me->x -= GAME_SPEED_X; /* move explosion by 1 step */

                /* tell the Game to render the current stage of Explosion */
                oie = Q_NEW(ObjectImageEvt, EXPLOSION_SIG);
                oie->x   = me->x + 1U;  /* x of explosion */
                oie->y   = (int8_t)((int)me->y - 4 + 2); /* y of explosion */
                oie->bmp = EXPLOSION0_BMP + (me->exp_ctr >> 2);
                QACTIVE_POST(AO_Tunnel, (QEvt *)oie, me);
                status = Q_HANDLED();
            }
            /* @(/2/3/3/2/1/0/1) */
            else {
                status = Q_TRAN(&Mine1_unused);
            }
            break;
        }
        default: {
            status = Q_SUPER(&Mine1_used);
            break;
        }
    }
    return status;
}
/* @(/2/3/3/2/2) ...........................................................*/
static QState Mine1_planted(Mine1 * const me, QEvt const * const e) {
    QState status;
    switch (e->sig) {
        /* @(/2/3/3/2/2/0) */
        case TIME_TICK_SIG: {
            /* @(/2/3/3/2/2/0/0) */
            if (me->x >= GAME_SPEED_X) {
                ObjectImageEvt *oie;
                me->x -= GAME_SPEED_X; /* move the mine 1 step */
                /* tell the Tunnel to draw the Mine */
                oie = Q_NEW(ObjectImageEvt, MINE_IMG_SIG);
                oie->x   = me->x;
                oie->y   = me->y;
                oie->bmp = MINE1_BMP;
                QACTIVE_POST(AO_Tunnel, (QEvt *)oie, me);
                status = Q_HANDLED();
            }
            /* @(/2/3/3/2/2/0/1) */
            else {
                status = Q_TRAN(&Mine1_unused);
            }
            break;
        }
        /* @(/2/3/3/2/2/1) */
        case SHIP_IMG_SIG: {
            uint8_t x   = Q_EVT_CAST(ObjectImageEvt)->x;
            uint8_t y   = Q_EVT_CAST(ObjectImageEvt)->y;
            uint8_t bmp = Q_EVT_CAST(ObjectImageEvt)->bmp;
            /* @(/2/3/3/2/2/1/0) */
            if (do_bitmaps_overlap(MINE1_BMP, me->x, me->y, bmp, x, y)) {
                static MineEvt const mine1_hit = {
                    { HIT_MINE_SIG, 0U, 0U }, /* the QEvt base instance */
                    1U  /* type of the mine (1 for Mine type-1) */
                };
                QACTIVE_POST(AO_Ship, (QEvt *)&mine1_hit, me);
                /* go straight to 'disabled' and let the Ship do
                 * the exploding */
                status = Q_TRAN(&Mine1_unused);
            }
            else {
                status = Q_UNHANDLED();
            }
            break;
        }
        /* @(/2/3/3/2/2/2) */
        case MISSILE_IMG_SIG: {
            uint8_t x   = Q_EVT_CAST(ObjectImageEvt)->x;
            uint8_t y   = Q_EVT_CAST(ObjectImageEvt)->y;
            uint8_t bmp = Q_EVT_CAST(ObjectImageEvt)->bmp;
            /* @(/2/3/3/2/2/2/0) */
            if (do_bitmaps_overlap(MINE1_BMP, me->x, me->y, bmp, x, y)) {
                static ScoreEvt const mine1_destroyed = {
                    { DESTROYED_MINE_SIG, 0U, 0U },  /* the QEvt base instance */
                    25U  /* score for destroying Mine type-1 */
                };
                QACTIVE_POST(AO_Missile, (QEvt *)&mine1_destroyed, me);
                status = Q_TRAN(&Mine1_exploding);
            }
            else {
                status = Q_UNHANDLED();
            }
            break;
        }
        default: {
            status = Q_SUPER(&Mine1_used);
            break;
        }
    }
    return status;
}
