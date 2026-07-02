"""
Rebalancing Engine

Stock-CIO
"""

from src.constants.rebalance_action import RebalanceAction
from src.models.portfolio import Portfolio
from src.models.rebalance_item import RebalanceItem
from src.models.rebalance_plan import RebalancePlan


class RebalancingEngine:
    """Portfolio Rebalancing Engine"""

    def create_plan(
        self,
        current: Portfolio,
        target: Portfolio,
    ) -> RebalancePlan:
        """
        Compare current portfolio with target portfolio
        and create a rebalancing plan.
        """

        plan = RebalancePlan()

        current_map = {
            position.ticker: position
            for position in current.positions
        }

        target_map = {
            position.ticker: position
            for position in target.positions
        }

        # 현재 보유 종목 기준
        for current_position in current.positions:

            target_position = target_map.get(
                current_position.ticker
            )

            if target_position is None:

                plan.add_item(
                    RebalanceItem(
                        ticker=current_position.ticker,
                        name=current_position.name,
                        current_weight=current_position.weight,
                        target_weight=0.0,
                        action=RebalanceAction.SELL,
                    )
                )

                continue

            if current_position.weight < target_position.weight:
                action = RebalanceAction.BUY

            elif current_position.weight > target_position.weight:
                action = RebalanceAction.SELL

            else:
                action = RebalanceAction.HOLD

            plan.add_item(
                RebalanceItem(
                    ticker=current_position.ticker,
                    name=current_position.name,
                    current_weight=current_position.weight,
                    target_weight=target_position.weight,
                    action=action,
                )
            )

        # 신규 편입 종목
        for target_position in target.positions:

            if target_position.ticker in current_map:
                continue

            plan.add_item(
                RebalanceItem(
                    ticker=target_position.ticker,
                    name=target_position.name,
                    current_weight=0.0,
                    target_weight=target_position.weight,
                    action=RebalanceAction.BUY,
                )
            )

        return plan